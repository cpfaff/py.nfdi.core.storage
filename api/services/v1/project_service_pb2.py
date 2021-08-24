# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/services/v1/project_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.services.v1 import project_service_models_pb2 as api_dot_services_dot_v1_dot_project__service__models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from grpc.gateway.protoc_gen_openapiv2.options import annotations_pb2 as grpc_dot_gateway_dot_protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/services/v1/project_service.proto',
  package='api.services.v1',
  syntax='proto3',
  serialized_options=b'\n4com.github.ScienceObjectsDB.java_api.api.services.v1B\022ProjectAPIServicesP\001Z2github.com/ScienceObjectsDB/go-api/api/services/v1\222A\234\007\022 \n\031ScienceObjectsDB REST API2\0030.1*\001\0022\020application/json:\020application/jsonRP\n\003403\022I\nGReturned when the user does not have permission to access the resource.R;\n\003404\0224\n*Returned when the resource does not exist.\022\006\n\004\232\002\001\007RW\n\003418\022P\n\rI\'m a teapot.\022?\n=\032;.grpc.gateway.examples.internal.proto.examplepb.NumericEnumR\233\002\n\003500\022\223\002\n\014Server error\022A\n?\032=.grpc.gateway.examples.internal.proto.examplepb.ErrorResponse\032\277\001\n\020X-Correlation-Id\022\252\001\n+Unique event identifier for server requests\022\006string\032\004uuid2&\"2438ac3c-37eb-4902-adef-ed16b4431030\"jE^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$Z\254\002\n\251\002\n\006OAuth2\022\236\002\010\003(\0012khttps://keycloak.infra.ingress.rancher.computational.bio/auth/realms/BioDataDB/protocol/openid-connect/auth:lhttps://keycloak.infra.ingress.rancher.computational.bio/auth/realms/BioDataDB/protocol/openid-connect/tokenB=\n\033\n\005email\022\022Grants read access\n\036\n\007profile\022\023Grants write accessb\034\n\032\n\006OAuth2\022\020\n\005email\n\007profile',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%api/services/v1/project_service.proto\x12\x0f\x61pi.services.v1\x1a,api/services/v1/project_service_models.proto\x1a\x1cgoogle/api/annotations.proto\x1a;grpc/gateway/protoc_gen_openapiv2/options/annotations.proto2\xcd\t\n\x0eProjectService\x12\x88\x01\n\rCreateProject\x12%.api.services.v1.CreateProjectRequest\x1a&.api.services.v1.CreateProjectResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/api/v1/project/createproject:\x01*\x12\x94\x01\n\x10\x41\x64\x64UserToProject\x12(.api.services.v1.AddUserToProjectRequest\x1a).api.services.v1.AddUserToProjectResponse\"+\x82\xd3\xe4\x93\x02%\" /api/v1/project/addusertoproject:\x01*\x12\x81\x01\n\x0e\x43reateAPIToken\x12&.api.services.v1.CreateAPITokenRequest\x1a\'.api.services.v1.CreateAPITokenResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/api/v1/createapitoken\x12\x9b\x01\n\x12GetProjectDatasets\x12*.api.services.v1.GetProjectDatasetsRequest\x1a+.api.services.v1.GetProjectDatasetsResponse\",\x82\xd3\xe4\x93\x02&\x12$/api/v1/project/{id}/projectdatasets\x12~\n\x0fGetUserProjects\x12\'.api.services.v1.GetUserProjectsRequest\x1a(.api.services.v1.GetUserProjectsResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/api/v1/projects\x12s\n\nGetProject\x12\".api.services.v1.GetProjectRequest\x1a#.api.services.v1.GetProjectResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/api/v1/project/{id}\x12r\n\x0bGetAPIToken\x12#.api.services.v1.GetAPITokenRequest\x1a$.api.services.v1.GetAPITokenResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/api/v1/apitoken\x12\x83\x01\n\rDeleteProject\x12%.api.services.v1.DeleteProjectRequest\x1a&.api.services.v1.DeleteProjectResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/api/v1/project/{id}/delete\x12\x87\x01\n\x0e\x44\x65leteAPIToken\x12&.api.services.v1.DeleteAPITokenRequest\x1a\'.api.services.v1.DeleteAPITokenResponse\"$\x82\xd3\xe4\x93\x02\x1e*\x1c/api/v1/apitoken/{id}/deleteB\xa0\x08\n4com.github.ScienceObjectsDB.java_api.api.services.v1B\x12ProjectAPIServicesP\x01Z2github.com/ScienceObjectsDB/go-api/api/services/v1\x92\x41\x9c\x07\x12 \n\x19ScienceObjectsDB REST API2\x03\x30.1*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonRP\n\x03\x34\x30\x33\x12I\nGReturned when the user does not have permission to access the resource.R;\n\x03\x34\x30\x34\x12\x34\n*Returned when the resource does not exist.\x12\x06\n\x04\x9a\x02\x01\x07RW\n\x03\x34\x31\x38\x12P\n\rI\'m a teapot.\x12?\n=\x1a;.grpc.gateway.examples.internal.proto.examplepb.NumericEnumR\x9b\x02\n\x03\x35\x30\x30\x12\x93\x02\n\x0cServer error\x12\x41\n?\x1a=.grpc.gateway.examples.internal.proto.examplepb.ErrorResponse\x1a\xbf\x01\n\x10X-Correlation-Id\x12\xaa\x01\n+Unique event identifier for server requests\x12\x06string\x1a\x04uuid2&\"2438ac3c-37eb-4902-adef-ed16b4431030\"jE^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$Z\xac\x02\n\xa9\x02\n\x06OAuth2\x12\x9e\x02\x08\x03(\x01\x32khttps://keycloak.infra.ingress.rancher.computational.bio/auth/realms/BioDataDB/protocol/openid-connect/auth:lhttps://keycloak.infra.ingress.rancher.computational.bio/auth/realms/BioDataDB/protocol/openid-connect/tokenB=\n\x1b\n\x05\x65mail\x12\x12Grants read access\n\x1e\n\x07profile\x12\x13Grants write accessb\x1c\n\x1a\n\x06OAuth2\x12\x10\n\x05\x65mail\n\x07profileb\x06proto3'
  ,
  dependencies=[api_dot_services_dot_v1_dot_project__service__models__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,grpc_dot_gateway_dot_protoc__gen__openapiv2_dot_options_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_PROJECTSERVICE = _descriptor.ServiceDescriptor(
  name='ProjectService',
  full_name='api.services.v1.ProjectService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=196,
  serialized_end=1425,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateProject',
    full_name='api.services.v1.ProjectService.CreateProject',
    index=0,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_project__service__models__pb2._CREATEPROJECTREQUEST,
    output_type=api_dot_services_dot_v1_dot_project__service__models__pb2._CREATEPROJECTRESPONSE,
    serialized_options=b'\202\323\344\223\002\"\"\035/api/v1/project/createproject:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddUserToProject',
    full_name='api.services.v1.ProjectService.AddUserToProject',
    index=1,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_project__service__models__pb2._ADDUSERTOPROJECTREQUEST,
    output_type=api_dot_services_dot_v1_dot_project__service__models__pb2._ADDUSERTOPROJECTRESPONSE,
    serialized_options=b'\202\323\344\223\002%\" /api/v1/project/addusertoproject:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateAPIToken',
    full_name='api.services.v1.ProjectService.CreateAPIToken',
    index=2,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_project__service__models__pb2._CREATEAPITOKENREQUEST,
    output_type=api_dot_services_dot_v1_dot_project__service__models__pb2._CREATEAPITOKENRESPONSE,
    serialized_options=b'\202\323\344\223\002\030\022\026/api/v1/createapitoken',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetProjectDatasets',
    full_name='api.services.v1.ProjectService.GetProjectDatasets',
    index=3,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_project__service__models__pb2._GETPROJECTDATASETSREQUEST,
    output_type=api_dot_services_dot_v1_dot_project__service__models__pb2._GETPROJECTDATASETSRESPONSE,
    serialized_options=b'\202\323\344\223\002&\022$/api/v1/project/{id}/projectdatasets',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserProjects',
    full_name='api.services.v1.ProjectService.GetUserProjects',
    index=4,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_project__service__models__pb2._GETUSERPROJECTSREQUEST,
    output_type=api_dot_services_dot_v1_dot_project__service__models__pb2._GETUSERPROJECTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\022\022\020/api/v1/projects',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetProject',
    full_name='api.services.v1.ProjectService.GetProject',
    index=5,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_project__service__models__pb2._GETPROJECTREQUEST,
    output_type=api_dot_services_dot_v1_dot_project__service__models__pb2._GETPROJECTRESPONSE,
    serialized_options=b'\202\323\344\223\002\026\022\024/api/v1/project/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAPIToken',
    full_name='api.services.v1.ProjectService.GetAPIToken',
    index=6,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_project__service__models__pb2._GETAPITOKENREQUEST,
    output_type=api_dot_services_dot_v1_dot_project__service__models__pb2._GETAPITOKENRESPONSE,
    serialized_options=b'\202\323\344\223\002\022\022\020/api/v1/apitoken',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteProject',
    full_name='api.services.v1.ProjectService.DeleteProject',
    index=7,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_project__service__models__pb2._DELETEPROJECTREQUEST,
    output_type=api_dot_services_dot_v1_dot_project__service__models__pb2._DELETEPROJECTRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\022\033/api/v1/project/{id}/delete',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAPIToken',
    full_name='api.services.v1.ProjectService.DeleteAPIToken',
    index=8,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_project__service__models__pb2._DELETEAPITOKENREQUEST,
    output_type=api_dot_services_dot_v1_dot_project__service__models__pb2._DELETEAPITOKENRESPONSE,
    serialized_options=b'\202\323\344\223\002\036*\034/api/v1/apitoken/{id}/delete',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROJECTSERVICE)

DESCRIPTOR.services_by_name['ProjectService'] = _PROJECTSERVICE

# @@protoc_insertion_point(module_scope)