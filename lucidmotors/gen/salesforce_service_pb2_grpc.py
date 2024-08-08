# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import salesforce_service_pb2 as salesforce__service__pb2


class SalesforceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServiceAppointmentsV1 = channel.unary_unary(
                '/mobilegateway.protos.SalesforceService/GetServiceAppointmentsV1',
                request_serializer=salesforce__service__pb2.GetServiceAppointmentsV1Request.SerializeToString,
                response_deserializer=salesforce__service__pb2.GetServiceAppointmentsV1Response.FromString,
                )
        self.GetServiceAppointmentSlots = channel.unary_unary(
                '/mobilegateway.protos.SalesforceService/GetServiceAppointmentSlots',
                request_serializer=salesforce__service__pb2.GetServiceAppointmentSlotsRequest.SerializeToString,
                response_deserializer=salesforce__service__pb2.GetServiceAppointmentSlotsResponse.FromString,
                )
        self.ReferralHistory = channel.unary_unary(
                '/mobilegateway.protos.SalesforceService/ReferralHistory',
                request_serializer=salesforce__service__pb2.ReferralHistoryRequest.SerializeToString,
                response_deserializer=salesforce__service__pb2.ReferralHistoryResponse.FromString,
                )


class SalesforceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetServiceAppointmentsV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceAppointmentSlots(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReferralHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SalesforceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServiceAppointmentsV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceAppointmentsV1,
                    request_deserializer=salesforce__service__pb2.GetServiceAppointmentsV1Request.FromString,
                    response_serializer=salesforce__service__pb2.GetServiceAppointmentsV1Response.SerializeToString,
            ),
            'GetServiceAppointmentSlots': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceAppointmentSlots,
                    request_deserializer=salesforce__service__pb2.GetServiceAppointmentSlotsRequest.FromString,
                    response_serializer=salesforce__service__pb2.GetServiceAppointmentSlotsResponse.SerializeToString,
            ),
            'ReferralHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.ReferralHistory,
                    request_deserializer=salesforce__service__pb2.ReferralHistoryRequest.FromString,
                    response_serializer=salesforce__service__pb2.ReferralHistoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mobilegateway.protos.SalesforceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SalesforceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetServiceAppointmentsV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.SalesforceService/GetServiceAppointmentsV1',
            salesforce__service__pb2.GetServiceAppointmentsV1Request.SerializeToString,
            salesforce__service__pb2.GetServiceAppointmentsV1Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceAppointmentSlots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.SalesforceService/GetServiceAppointmentSlots',
            salesforce__service__pb2.GetServiceAppointmentSlotsRequest.SerializeToString,
            salesforce__service__pb2.GetServiceAppointmentSlotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReferralHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.SalesforceService/ReferralHistory',
            salesforce__service__pb2.ReferralHistoryRequest.SerializeToString,
            salesforce__service__pb2.ReferralHistoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
