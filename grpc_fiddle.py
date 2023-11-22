import logging
import getpass

import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)
import login_session_pb2
import login_session_pb2_grpc


def main():
    username = input("Username: ")
    password = getpass.getpass()

    with grpc.secure_channel("mobile.deneb.prod.infotainment.pdx.atieva.com", grpc.ssl_channel_credentials()) as channel:
        stub = login_session_pb2_grpc.LoginSessionStub(channel)
        req = login_session_pb2.LoginRequest(
            username=username,
            password=password,
            notification_channel_type=login_session_pb2.NotificationChannelType.NOTIFICATION_CHANNEL_ONE,
            os=login_session_pb2.Os.OS_IOS,
            locale='en_US',
            device_id='python-lucidmotors',
        )
        response = stub.Login(req)
        print(response)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
