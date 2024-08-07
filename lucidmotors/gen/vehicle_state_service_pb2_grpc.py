# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import vehicle_state_service_pb2 as vehicle__state__service__pb2


class VehicleStateServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ApplySoftwareUpdate = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/ApplySoftwareUpdate',
                request_serializer=vehicle__state__service__pb2.ApplySoftwareUpdateRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.ApplySoftwareUpdateResponse.FromString,
                )
        self.CancelScheduledUpdate = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/CancelScheduledUpdate',
                request_serializer=vehicle__state__service__pb2.CancelScheduledUpdateRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.CancelScheduledUpdateResponse.FromString,
                )
        self.ChargeControl = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/ChargeControl',
                request_serializer=vehicle__state__service__pb2.ChargeControlRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.ChargeControlResponse.FromString,
                )
        self.ControlChargePort = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/ControlChargePort',
                request_serializer=vehicle__state__service__pb2.ControlChargePortRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.ControlChargePortResponse.FromString,
                )
        self.DoorLocksControl = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/DoorLocksControl',
                request_serializer=vehicle__state__service__pb2.DoorLocksControlRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.DoorLocksControlResponse.FromString,
                )
        self.FrontCargoControl = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/FrontCargoControl',
                request_serializer=vehicle__state__service__pb2.FrontCargoControlRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.FrontCargoControlResponse.FromString,
                )
        self.GetDocumentInfo = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/GetDocumentInfo',
                request_serializer=vehicle__state__service__pb2.GetDocumentInfoRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.GetDocumentInfoResponse.FromString,
                )
        self.GetVehicleState = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/GetVehicleState',
                request_serializer=vehicle__state__service__pb2.GetVehicleStateRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.GetVehicleStateResponse.FromString,
                )
        self.HonkHorn = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/HonkHorn',
                request_serializer=vehicle__state__service__pb2.HonkHornRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.HonkHornResponse.FromString,
                )
        self.HvacDefrostControl = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/HvacDefrostControl',
                request_serializer=vehicle__state__service__pb2.HvacDefrostControlRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.HvacDefrostControlResponse.FromString,
                )
        self.LightsControl = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/LightsControl',
                request_serializer=vehicle__state__service__pb2.LightsControlRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.LightsControlResponse.FromString,
                )
        self.RearCargoControl = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/RearCargoControl',
                request_serializer=vehicle__state__service__pb2.RearCargoControlRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.RearCargoControlResponse.FromString,
                )
        self.SecurityAlarmControl = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/SecurityAlarmControl',
                request_serializer=vehicle__state__service__pb2.SecurityAlarmControlRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.SecurityAlarmControlResponse.FromString,
                )
        self.SetCabinTemperature = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/SetCabinTemperature',
                request_serializer=vehicle__state__service__pb2.SetCabinTemperatureRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.SetCabinTemperatureResponse.FromString,
                )
        self.SetChargeLimit = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/SetChargeLimit',
                request_serializer=vehicle__state__service__pb2.SetChargeLimitRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.SetChargeLimitResponse.FromString,
                )
        self.WakeupVehicle = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/WakeupVehicle',
                request_serializer=vehicle__state__service__pb2.WakeupVehicleRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.WakeupVehicleResponse.FromString,
                )
        self.SetBatteryPrecon = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/SetBatteryPrecon',
                request_serializer=vehicle__state__service__pb2.SetBatteryPreconRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.SetBatteryPreconResponse.FromString,
                )
        self.SetDischargeSoeLimit = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/SetDischargeSoeLimit',
                request_serializer=vehicle__state__service__pb2.SetDischargeSoeLimitRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.SetDischargeSoeLimitResponse.FromString,
                )
        self.DischargeControl = channel.unary_unary(
                '/mobilegateway.protos.VehicleStateService/DischargeControl',
                request_serializer=vehicle__state__service__pb2.DischargeControlRequest.SerializeToString,
                response_deserializer=vehicle__state__service__pb2.DischargeControlResponse.FromString,
                )


class VehicleStateServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ApplySoftwareUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelScheduledUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChargeControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ControlChargePort(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DoorLocksControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FrontCargoControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDocumentInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVehicleState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HonkHorn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HvacDefrostControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LightsControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RearCargoControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SecurityAlarmControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCabinTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetChargeLimit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WakeupVehicle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetBatteryPrecon(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDischargeSoeLimit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DischargeControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VehicleStateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ApplySoftwareUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplySoftwareUpdate,
                    request_deserializer=vehicle__state__service__pb2.ApplySoftwareUpdateRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.ApplySoftwareUpdateResponse.SerializeToString,
            ),
            'CancelScheduledUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelScheduledUpdate,
                    request_deserializer=vehicle__state__service__pb2.CancelScheduledUpdateRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.CancelScheduledUpdateResponse.SerializeToString,
            ),
            'ChargeControl': grpc.unary_unary_rpc_method_handler(
                    servicer.ChargeControl,
                    request_deserializer=vehicle__state__service__pb2.ChargeControlRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.ChargeControlResponse.SerializeToString,
            ),
            'ControlChargePort': grpc.unary_unary_rpc_method_handler(
                    servicer.ControlChargePort,
                    request_deserializer=vehicle__state__service__pb2.ControlChargePortRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.ControlChargePortResponse.SerializeToString,
            ),
            'DoorLocksControl': grpc.unary_unary_rpc_method_handler(
                    servicer.DoorLocksControl,
                    request_deserializer=vehicle__state__service__pb2.DoorLocksControlRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.DoorLocksControlResponse.SerializeToString,
            ),
            'FrontCargoControl': grpc.unary_unary_rpc_method_handler(
                    servicer.FrontCargoControl,
                    request_deserializer=vehicle__state__service__pb2.FrontCargoControlRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.FrontCargoControlResponse.SerializeToString,
            ),
            'GetDocumentInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDocumentInfo,
                    request_deserializer=vehicle__state__service__pb2.GetDocumentInfoRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.GetDocumentInfoResponse.SerializeToString,
            ),
            'GetVehicleState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVehicleState,
                    request_deserializer=vehicle__state__service__pb2.GetVehicleStateRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.GetVehicleStateResponse.SerializeToString,
            ),
            'HonkHorn': grpc.unary_unary_rpc_method_handler(
                    servicer.HonkHorn,
                    request_deserializer=vehicle__state__service__pb2.HonkHornRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.HonkHornResponse.SerializeToString,
            ),
            'HvacDefrostControl': grpc.unary_unary_rpc_method_handler(
                    servicer.HvacDefrostControl,
                    request_deserializer=vehicle__state__service__pb2.HvacDefrostControlRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.HvacDefrostControlResponse.SerializeToString,
            ),
            'LightsControl': grpc.unary_unary_rpc_method_handler(
                    servicer.LightsControl,
                    request_deserializer=vehicle__state__service__pb2.LightsControlRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.LightsControlResponse.SerializeToString,
            ),
            'RearCargoControl': grpc.unary_unary_rpc_method_handler(
                    servicer.RearCargoControl,
                    request_deserializer=vehicle__state__service__pb2.RearCargoControlRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.RearCargoControlResponse.SerializeToString,
            ),
            'SecurityAlarmControl': grpc.unary_unary_rpc_method_handler(
                    servicer.SecurityAlarmControl,
                    request_deserializer=vehicle__state__service__pb2.SecurityAlarmControlRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.SecurityAlarmControlResponse.SerializeToString,
            ),
            'SetCabinTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCabinTemperature,
                    request_deserializer=vehicle__state__service__pb2.SetCabinTemperatureRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.SetCabinTemperatureResponse.SerializeToString,
            ),
            'SetChargeLimit': grpc.unary_unary_rpc_method_handler(
                    servicer.SetChargeLimit,
                    request_deserializer=vehicle__state__service__pb2.SetChargeLimitRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.SetChargeLimitResponse.SerializeToString,
            ),
            'WakeupVehicle': grpc.unary_unary_rpc_method_handler(
                    servicer.WakeupVehicle,
                    request_deserializer=vehicle__state__service__pb2.WakeupVehicleRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.WakeupVehicleResponse.SerializeToString,
            ),
            'SetBatteryPrecon': grpc.unary_unary_rpc_method_handler(
                    servicer.SetBatteryPrecon,
                    request_deserializer=vehicle__state__service__pb2.SetBatteryPreconRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.SetBatteryPreconResponse.SerializeToString,
            ),
            'SetDischargeSoeLimit': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDischargeSoeLimit,
                    request_deserializer=vehicle__state__service__pb2.SetDischargeSoeLimitRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.SetDischargeSoeLimitResponse.SerializeToString,
            ),
            'DischargeControl': grpc.unary_unary_rpc_method_handler(
                    servicer.DischargeControl,
                    request_deserializer=vehicle__state__service__pb2.DischargeControlRequest.FromString,
                    response_serializer=vehicle__state__service__pb2.DischargeControlResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mobilegateway.protos.VehicleStateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VehicleStateService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ApplySoftwareUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/ApplySoftwareUpdate',
            vehicle__state__service__pb2.ApplySoftwareUpdateRequest.SerializeToString,
            vehicle__state__service__pb2.ApplySoftwareUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelScheduledUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/CancelScheduledUpdate',
            vehicle__state__service__pb2.CancelScheduledUpdateRequest.SerializeToString,
            vehicle__state__service__pb2.CancelScheduledUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChargeControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/ChargeControl',
            vehicle__state__service__pb2.ChargeControlRequest.SerializeToString,
            vehicle__state__service__pb2.ChargeControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ControlChargePort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/ControlChargePort',
            vehicle__state__service__pb2.ControlChargePortRequest.SerializeToString,
            vehicle__state__service__pb2.ControlChargePortResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DoorLocksControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/DoorLocksControl',
            vehicle__state__service__pb2.DoorLocksControlRequest.SerializeToString,
            vehicle__state__service__pb2.DoorLocksControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FrontCargoControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/FrontCargoControl',
            vehicle__state__service__pb2.FrontCargoControlRequest.SerializeToString,
            vehicle__state__service__pb2.FrontCargoControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDocumentInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/GetDocumentInfo',
            vehicle__state__service__pb2.GetDocumentInfoRequest.SerializeToString,
            vehicle__state__service__pb2.GetDocumentInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVehicleState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/GetVehicleState',
            vehicle__state__service__pb2.GetVehicleStateRequest.SerializeToString,
            vehicle__state__service__pb2.GetVehicleStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HonkHorn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/HonkHorn',
            vehicle__state__service__pb2.HonkHornRequest.SerializeToString,
            vehicle__state__service__pb2.HonkHornResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HvacDefrostControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/HvacDefrostControl',
            vehicle__state__service__pb2.HvacDefrostControlRequest.SerializeToString,
            vehicle__state__service__pb2.HvacDefrostControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LightsControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/LightsControl',
            vehicle__state__service__pb2.LightsControlRequest.SerializeToString,
            vehicle__state__service__pb2.LightsControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RearCargoControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/RearCargoControl',
            vehicle__state__service__pb2.RearCargoControlRequest.SerializeToString,
            vehicle__state__service__pb2.RearCargoControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SecurityAlarmControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/SecurityAlarmControl',
            vehicle__state__service__pb2.SecurityAlarmControlRequest.SerializeToString,
            vehicle__state__service__pb2.SecurityAlarmControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCabinTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/SetCabinTemperature',
            vehicle__state__service__pb2.SetCabinTemperatureRequest.SerializeToString,
            vehicle__state__service__pb2.SetCabinTemperatureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetChargeLimit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/SetChargeLimit',
            vehicle__state__service__pb2.SetChargeLimitRequest.SerializeToString,
            vehicle__state__service__pb2.SetChargeLimitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WakeupVehicle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/WakeupVehicle',
            vehicle__state__service__pb2.WakeupVehicleRequest.SerializeToString,
            vehicle__state__service__pb2.WakeupVehicleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetBatteryPrecon(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/SetBatteryPrecon',
            vehicle__state__service__pb2.SetBatteryPreconRequest.SerializeToString,
            vehicle__state__service__pb2.SetBatteryPreconResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDischargeSoeLimit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/SetDischargeSoeLimit',
            vehicle__state__service__pb2.SetDischargeSoeLimitRequest.SerializeToString,
            vehicle__state__service__pb2.SetDischargeSoeLimitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DischargeControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mobilegateway.protos.VehicleStateService/DischargeControl',
            vehicle__state__service__pb2.DischargeControlRequest.SerializeToString,
            vehicle__state__service__pb2.DischargeControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
