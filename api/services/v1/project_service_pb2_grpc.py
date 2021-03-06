# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.services.v1 import project_service_models_pb2 as api_dot_services_dot_v1_dot_project__service__models__pb2


class ProjectServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProject = channel.unary_unary(
                '/api.services.v1.ProjectService/CreateProject',
                request_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.CreateProjectResponse.FromString,
                )
        self.AddUserToProject = channel.unary_unary(
                '/api.services.v1.ProjectService/AddUserToProject',
                request_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.AddUserToProjectRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.AddUserToProjectResponse.FromString,
                )
        self.CreateAPIToken = channel.unary_unary(
                '/api.services.v1.ProjectService/CreateAPIToken',
                request_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.CreateAPITokenRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.CreateAPITokenResponse.FromString,
                )
        self.GetProjectDatasets = channel.unary_unary(
                '/api.services.v1.ProjectService/GetProjectDatasets',
                request_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectDatasetsRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectDatasetsResponse.FromString,
                )
        self.GetUserProjects = channel.unary_unary(
                '/api.services.v1.ProjectService/GetUserProjects',
                request_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetUserProjectsRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetUserProjectsResponse.FromString,
                )
        self.GetProject = channel.unary_unary(
                '/api.services.v1.ProjectService/GetProject',
                request_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectResponse.FromString,
                )
        self.GetAPIToken = channel.unary_unary(
                '/api.services.v1.ProjectService/GetAPIToken',
                request_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetAPITokenRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetAPITokenResponse.FromString,
                )
        self.DeleteProject = channel.unary_unary(
                '/api.services.v1.ProjectService/DeleteProject',
                request_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteProjectRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteProjectResponse.FromString,
                )
        self.DeleteAPIToken = channel.unary_unary(
                '/api.services.v1.ProjectService/DeleteAPIToken',
                request_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteAPITokenRequest.SerializeToString,
                response_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteAPITokenResponse.FromString,
                )


class ProjectServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateProject(self, request, context):
        """CreateProject creates a new projects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUserToProject(self, request, context):
        """AddUserToProject Adds a new user to a given project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAPIToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProjectDatasets(self, request, context):
        """GetProjectDatasets Returns all datasets that belong to a certain project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserProjects(self, request, context):
        """GetUserProjects Returns all projects that a specified user has access to
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAPIToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProject(self, request, context):
        """DeleteProject Deletes a specific project
        Will also delete all associated resources (Datasets/Objects/etc...) both from objects storage and the database
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAPIToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.CreateProjectRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.CreateProjectResponse.SerializeToString,
            ),
            'AddUserToProject': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUserToProject,
                    request_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.AddUserToProjectRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.AddUserToProjectResponse.SerializeToString,
            ),
            'CreateAPIToken': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAPIToken,
                    request_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.CreateAPITokenRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.CreateAPITokenResponse.SerializeToString,
            ),
            'GetProjectDatasets': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProjectDatasets,
                    request_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectDatasetsRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectDatasetsResponse.SerializeToString,
            ),
            'GetUserProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserProjects,
                    request_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetUserProjectsRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetUserProjectsResponse.SerializeToString,
            ),
            'GetProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProject,
                    request_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectResponse.SerializeToString,
            ),
            'GetAPIToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIToken,
                    request_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetAPITokenRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.GetAPITokenResponse.SerializeToString,
            ),
            'DeleteProject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProject,
                    request_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteProjectRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteProjectResponse.SerializeToString,
            ),
            'DeleteAPIToken': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAPIToken,
                    request_deserializer=api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteAPITokenRequest.FromString,
                    response_serializer=api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteAPITokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.services.v1.ProjectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.ProjectService/CreateProject',
            api_dot_services_dot_v1_dot_project__service__models__pb2.CreateProjectRequest.SerializeToString,
            api_dot_services_dot_v1_dot_project__service__models__pb2.CreateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUserToProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.ProjectService/AddUserToProject',
            api_dot_services_dot_v1_dot_project__service__models__pb2.AddUserToProjectRequest.SerializeToString,
            api_dot_services_dot_v1_dot_project__service__models__pb2.AddUserToProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAPIToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.ProjectService/CreateAPIToken',
            api_dot_services_dot_v1_dot_project__service__models__pb2.CreateAPITokenRequest.SerializeToString,
            api_dot_services_dot_v1_dot_project__service__models__pb2.CreateAPITokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProjectDatasets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.ProjectService/GetProjectDatasets',
            api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectDatasetsRequest.SerializeToString,
            api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectDatasetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.ProjectService/GetUserProjects',
            api_dot_services_dot_v1_dot_project__service__models__pb2.GetUserProjectsRequest.SerializeToString,
            api_dot_services_dot_v1_dot_project__service__models__pb2.GetUserProjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.ProjectService/GetProject',
            api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectRequest.SerializeToString,
            api_dot_services_dot_v1_dot_project__service__models__pb2.GetProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAPIToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.ProjectService/GetAPIToken',
            api_dot_services_dot_v1_dot_project__service__models__pb2.GetAPITokenRequest.SerializeToString,
            api_dot_services_dot_v1_dot_project__service__models__pb2.GetAPITokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.ProjectService/DeleteProject',
            api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteProjectRequest.SerializeToString,
            api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAPIToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.services.v1.ProjectService/DeleteAPIToken',
            api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteAPITokenRequest.SerializeToString,
            api_dot_services_dot_v1_dot_project__service__models__pb2.DeleteAPITokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
