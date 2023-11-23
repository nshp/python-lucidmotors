from typing import Any
from google.protobuf.unknown_fields import UnknownFieldSet

import uuid
import grpc
import ipdb
import logging
import getpass
import google._upb
import google.protobuf

from lucidmotors.gen import login_session_pb2
from lucidmotors.gen import login_session_pb2_grpc

wire_types = {
    0: 'varint',
    1: 'fixed-64bit',
    2: 'length-delimited',
    3: 'group-start',
    4: 'group-end',
    5: 'fixed-32bit',
}

def message_dump_recursive(message: Any, depth: int = 0):
    if isinstance(message, (google._upb._message.RepeatedScalarContainer, google._upb._message.RepeatedCompositeContainer)):
        for elem in message:
            message_dump_recursive(elem, depth=depth)
        return

    if not isinstance(message, google.protobuf.message.Message):
        return

    indent = ' ' * depth
    print(f'{indent}{type(message)}:')

    depth += 1
    indent = ' ' * depth

    for field in UnknownFieldSet(message):
        wire_type = wire_types[field.wire_type]
        print(f'{indent}Unknown field {field.field_number} wire type {wire_type}: {field.data!r}')

    for descriptor, field in message.ListFields():
        if isinstance(field, (google.protobuf.message.Message, google._upb._message.RepeatedScalarContainer, google._upb._message.RepeatedCompositeContainer)):
            field_desc_short = ''
        elif descriptor.enum_type is not None:
            # TODO: Handle a list of enum, like LoginResponse.subscriptions
            enum = descriptor.enum_type
            if field in enum.values_by_number:
                name = enum.values_by_number[field].name
                field_desc_short = f'{name} ({field})'
            else:
                field_desc_short = f'UNKNOWN ENUMERATOR: {field}'
        else:
            field_desc_short = str(field)
        print(f'{indent}Field {descriptor.number}, {descriptor.name}: {field_desc_short}')
        message_dump_recursive(field, depth=depth)


def main():
    username = input("Username: ")
    password = getpass.getpass()

    with grpc.secure_channel("mobile.deneb.prod.infotainment.pdx.atieva.com", grpc.ssl_channel_credentials()) as channel:
        stub = login_session_pb2_grpc.LoginSessionStub(channel)
        device_id = f'{uuid.getnode():x}'
        req = login_session_pb2.LoginRequest(
            username=username,
            password=password,
            notification_channel_type=login_session_pb2.NotificationChannelType.NOTIFICATION_CHANNEL_ONE,
            notification_device_token=device_id,
            os=login_session_pb2.Os.OS_IOS,
            locale='en_US',
            client_name='python-lucidmotors',
            device_id=device_id,
        )
        response = stub.Login(req)
        message_dump_recursive(response)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
