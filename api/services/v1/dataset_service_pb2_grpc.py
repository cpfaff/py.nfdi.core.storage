# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.services.v1 import dataset_service_models_pb2 as api_dot_services_dot_v1_dot_dataset__service__models__pb2


class DatasetServiceStub(object):
    """Dataset management service
    Manages all dataset related services
    All data objects are associated with one data dataset
    Dataset versions group these data objects, which makes them reusable
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateDataset = channel.unary_unary(
                '/api.services.v1.DatasetService/CreateDataset',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.CreateDatasetRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.CreateDatasetResponse.FromString,
                )
        self.GetDataset = channel.unary_unary(
                '/api.services.v1.DatasetService/GetDataset',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetResponse.FromString,
                )
        self.GetDatasetVersions = channel.unary_unary(
                '/api.services.v1.DatasetService/GetDatasetVersions',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionsRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionsResponse.FromString,
                )
        self.GetDatasetObjectGroups = channel.unary_unary(
                '/api.services.v1.DatasetService/GetDatasetObjectGroups',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetObjectGroupsRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetObjectGroupsResponse.FromString,
                )
        self.GetObjectGroupsStream = channel.unary_unary(
                '/api.services.v1.DatasetService/GetObjectGroupsStream',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsStreamLinkRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsStreamLinkResponse.FromString,
                )
        self.UpdateDatasetField = channel.unary_unary(
                '/api.services.v1.DatasetService/UpdateDatasetField',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.UpdateDatasetFieldRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.UpdateDatasetFieldResponse.FromString,
                )
        self.DeleteDataset = channel.unary_unary(
                '/api.services.v1.DatasetService/DeleteDataset',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetResponse.FromString,
                )
        self.GetObjectGroupsInDateRange = channel.unary_unary(
                '/api.services.v1.DatasetService/GetObjectGroupsInDateRange',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsInDateRangeRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsInDateRangeResponse.FromString,
                )
        self.ReleaseDatasetVersion = channel.unary_unary(
                '/api.services.v1.DatasetService/ReleaseDatasetVersion',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.ReleaseDatasetVersionRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.ReleaseDatasetVersionResponse.FromString,
                )
        self.GetDatasetVersion = channel.unary_unary(
                '/api.services.v1.DatasetService/GetDatasetVersion',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionResponse.FromString,
                )
        self.GetDatasetVersionObjectGroups = channel.unary_unary(
                '/api.services.v1.DatasetService/GetDatasetVersionObjectGroups',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionObjectGroupsRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionObjectGroupsResponse.FromString,
                )
        self.DeleteDatasetVersion = channel.unary_unary(
                '/api.services.v1.DatasetService/DeleteDatasetVersion',
                request_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetVersionRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetVersionResponse.FromString,
                )


class DatasetServiceServicer(object):
    """Dataset management service
    Manages all dataset related services
    All data objects are associated with one data dataset
    Dataset versions group these data objects, which makes them reusable
    """

    def CreateDataset(self, request, context):
        """CreateNewDataset Creates a new dataset and associates it with a dataset
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDataset(self, request, context):
        """Dataset Returns a specific dataset
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDatasetVersions(self, request, context):
        """Lists Versions of a dataset
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDatasetObjectGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectGroupsStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDatasetField(self, request, context):
        """Updates a field of a dataset
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDataset(self, request, context):
        """DeleteDataset Delete a dataset
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectGroupsInDateRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReleaseDatasetVersion(self, request, context):
        """---------------------------------------------------------------------------------------
        Dataset version calls

        ReleaseDatasetVersion Release a new dataset version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDatasetVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDatasetVersionObjectGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDatasetVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatasetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateDataset': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDataset,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.CreateDatasetRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.CreateDatasetResponse.SerializeToString,
            ),
            'GetDataset': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDataset,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetResponse.SerializeToString,
            ),
            'GetDatasetVersions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatasetVersions,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionsRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionsResponse.SerializeToString,
            ),
            'GetDatasetObjectGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatasetObjectGroups,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetObjectGroupsRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetObjectGroupsResponse.SerializeToString,
            ),
            'GetObjectGroupsStream': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectGroupsStream,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsStreamLinkRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsStreamLinkResponse.SerializeToString,
            ),
            'UpdateDatasetField': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDatasetField,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.UpdateDatasetFieldRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.UpdateDatasetFieldResponse.SerializeToString,
            ),
            'DeleteDataset': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDataset,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetResponse.SerializeToString,
            ),
            'GetObjectGroupsInDateRange': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectGroupsInDateRange,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsInDateRangeRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsInDateRangeResponse.SerializeToString,
            ),
            'ReleaseDatasetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.ReleaseDatasetVersion,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.ReleaseDatasetVersionRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.ReleaseDatasetVersionResponse.SerializeToString,
            ),
            'GetDatasetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatasetVersion,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionResponse.SerializeToString,
            ),
            'GetDatasetVersionObjectGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatasetVersionObjectGroups,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionObjectGroupsRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionObjectGroupsResponse.SerializeToString,
            ),
            'DeleteDatasetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDatasetVersion,
                    request_deserializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetVersionRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetVersionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.services.v1.DatasetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatasetService(object):
    """Dataset management service
    Manages all dataset related services
    All data objects are associated with one data dataset
    Dataset versions group these data objects, which makes them reusable
    """

    @staticmethod
    def CreateDataset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/CreateDataset',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.CreateDatasetRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.CreateDatasetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDataset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/GetDataset',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDatasetVersions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/GetDatasetVersions',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionsRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDatasetObjectGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/GetDatasetObjectGroups',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetObjectGroupsRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetObjectGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectGroupsStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/GetObjectGroupsStream',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsStreamLinkRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsStreamLinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDatasetField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/UpdateDatasetField',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.UpdateDatasetFieldRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.UpdateDatasetFieldResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDataset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/DeleteDataset',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectGroupsInDateRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/GetObjectGroupsInDateRange',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsInDateRangeRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetObjectGroupsInDateRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReleaseDatasetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/ReleaseDatasetVersion',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.ReleaseDatasetVersionRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.ReleaseDatasetVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDatasetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/GetDatasetVersion',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDatasetVersionObjectGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/GetDatasetVersionObjectGroups',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionObjectGroupsRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.GetDatasetVersionObjectGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDatasetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.DatasetService/DeleteDatasetVersion',
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetVersionRequest.SerializeToString,
            api_dot_services_dot_v1_dot_dataset__service__models__pb2.DeleteDatasetVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)