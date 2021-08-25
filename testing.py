import grpc
import requests

#  Order: CreateProject -> CreateDataset -> CreateObjectGroup -> UploadFile

# create a project
import api.services.v1.project_service_pb2_grpc as project_service_pb2_grpc
import api.services.v1.project_service_models_pb2 as project_service_models_pb2

# create dataset
import api.services.v1.dataset_service_pb2_grpc as dataset_service_pb2_grpc
import api.services.v1.dataset_service_models_pb2 as dataset_service_models_pb2

# dataset objects
import api.services.v1.dataset_object_service_pb2_grpc as dataset_object_service_pb2_grpc
import api.services.v1.dataset_object_service_models_pb2 as dataset_object_service_models_pb2

# upload dataset
import api.services.v1.object_load_pb2_grpc as object_load_pb2_grpc
import api.services.v1.object_load_models_pb2 as object_load_models_pb2

class NfdiCoreStorage:

    """
    A NfdiCoreStorage representation providing convenient access to the API
    """

    def __init__(self, api_url=None, root_cert=None, channel=None):
        """ Initializing the core storabe object  """
        if api_url is None:
            self.api_url = "api.core-server-dev.m1.k8s.computational.bio"
        else:
            self.api_url = api_url
        if root_cert is None:
            self.root_cert = "lets_encrypt_cert.pem"
        else:
            self.root_cert = root_cert
        self.channel = channel

        self.connect()

    # instance methods 

    ## project

    def create_project(self, name, description, token=None):
        """
        Creating projects
        """
        stub =  project_service_pb2_grpc.ProjectServiceStub(self.channel)
        response, call = stub.CreateProject.with_call(
            project_service_models_pb2.CreateProjectRequest(name=name, description=description),
            metadata=( ('api_token', token),
            ))
        return(response)

    def get_project(self, id, token=None):
        stub =  project_service_pb2_grpc.ProjectServiceStub(self.channel)
        response, call = stub.GetProject.with_call(
            project_service_models_pb2.GetProjectRequest(id = id),
            metadata=( ('api_token', token),
            ))
        return(response)

        #  GetProject
        #  CreateProject
        #  AddUserToProject
        #  CreateAPIToken
        #  GetProjectDatasets
        #  GetUserProjects
        #  GetAPIToken
        #  DeleteProject
        #  DeleteAPIToken

    def create_project_token(self, id, token=None):
        """
        Creating tokens inside of a project
        """
        stub =  project_service_pb2_grpc.ProjectServiceStub(self.channel)
        response, call = stub.CreateAPIToken.with_call(
            project_service_models_pb2.CreateAPITokenRequest(id = id),
            metadata=(('api_token', token),
            ))
        return(response)


    def create_dataset(self, name, project_id, token=None):
        """
        Create a dataset in a project
        """
        stub = dataset_service_pb2_grpc.DatasetServiceStub(self.channel)
        response, call = stub.CreateDataset.with_call(
            dataset_service_models_pb2.CreateDatasetRequest(name=name, project_id=project_id),
            metadata=(
                ('api_token', token),
            ))
        return(response)

    def create_object_group(self, name, dataset_id, token=None, objects=None):
        # todo: here compose the iterable of objects then pass this down to the CreateObjectGroupRequest
        stub = dataset_object_service_pb2_grpc.DatasetObjectsServiceStub(self.channel)
        response, call = stub.CreateObjectGroup.with_call(
            dataset_object_service_models_pb2.CreateObjectGroupRequest(name=name, dataset_id=dataset_id, objects =  [dataset_object_service_models_pb2.CreateObjectRequest(filename = "Test.txt", filetype = "txt")]),
            metadata=(
                ('api_token', token),
            ),
        )
        return(response)

    def get_object_group(self, object_group_id, token=None):
        stub = dataset_object_service_pb2_grpc.DatasetObjectsServiceStub(self.channel)
        response, call = stub.GetObjectGroup.with_call(
            dataset_object_service_models_pb2.GetObjectGroupRequest(id=object_group_id),
            metadata=(
                ('api_token', token),
            ))
        return(response)

    def create_upload_link(self, object_id, token=None):
        stub = object_load_pb2_grpc.ObjectLoadServiceStub(self.channel)
        response, call = stub.CreateUploadLink.with_call(
            object_load_models_pb2.CreateUploadLinkRequest(id = object_id),
            metadata=(
                ('api_token', token),
            ))
        return(response)


    # private methods 
    def connect(self):
        with open(self.root_cert, 'rb') as file:
                credentials = grpc.ssl_channel_credentials(root_certificates = file.read())
        channel = grpc.secure_channel(self.api_url, credentials = credentials)
        self.channel = channel

    # special methods 
    def __repr__(self):
        return f"NFDI core storage api connector. Associated to {self.api_url}"

    def __str__(self):
        return f"NFDI core storage api connector. Associated to {self.api_url}"

#  if __name__ == "__main__":
    #  pass

# setup
store = NfdiCoreStorage()
store

#  Order: CreateProject (Do it online) -> CreateDataset -> CreateObjectGroup -> UploadFile

#  CreateProject (You cannot create a project from here. You need the UI and add an api token)
#  token = "Tke7/Ojo00qKEtF/Dr7VvO/KUC3VCUlbHn3AaLPvjpQAy4M+WmYJjXJbbslc"
#  project_id = 686990469178916865
#  project = store.create_project(name = "A new project", description = "with a brandnew description", token="Tke7/Ojo00qKEtF/Dr7VvO/KUC3VCUlbHn3AaLPvjpQAy4M+WmYJjXJbbslc")
#  project


# * but this requires an API token. So I can only create projects from my scripts when I have
#   an api token already. An API token is however is associated with a project. So finally I can only
#   create datasets when I have created a project manually on the page adding an api token to 
#   it?

#  project = store.create_project(name = "A new project", description = "with a brandnew description", token = token)
#  project

# * that way it works. But as API tokens are project specific creating a dataset in the next step requires a 
#   project specific token. The project we just created however does not inherit the token that we passed in
#   it does not have a token that we could use to authenticate that we are allowed to create a dataset in here. 

#  CreateDataset

token = "Tke7/Ojo00qKEtF/Dr7VvO/KUC3VCUlbHn3AaLPvjpQAy4M+WmYJjXJbbslc"
project_id = 686990469178916865
dataset = store.create_dataset(name = "A new project dataset", project_id = project_id, token=token)

# * This fails. The new project that we created does not have any token associated. Also we cannot use
#   the same token that we have used to create the project (not inherited). We first need to go 
#   to the web page again and create a project specific token and note it down as this is needed 
#   as authorization to create e.g. datasets in that project.

#  dataset = store.create_dataset(name = "A new project dataset", project_id = project_id, token=token)
#  dataset

# *  we can create tokens inside project using the function below. However this does not work for new projects as
#    the create_token funktion requires a token for authorization in that project. So initially we have to add a
#    first token manually in that project in order to use that token function to finally create more token in the 
#    project programmatically. Ooo 

#  store.create_project_token(id = project, token = "PZOtu0R9)w6RT~NoCggLpUk3ICjkfW")

#  CreateObjectGroup

#  in create object group gibt es objects parameter. Create objects mit reingeben
# GetObjectGroup
# in der rückgabe gibt es objects
# für jedes dieser objekte gibt es eine ide

new_object_grouop = store.create_object_group(name = "My new object group", dataset_id = dataset.id, token = token)
object_group = store.get_object_group(object_group_id=new_object_grouop.object_group_id, token = token)
object_group

# TODO: figure out how to extract ids from that json like return value  og get objet group
#  dir(object_group)
#  json.loads(object_group.SerializeToString())

# upload a file
upload_url = store.create_upload_link(object_id =687500400419241987, token=token)
link = upload_url.upload_link

file = {'file': open('testing.py','rb')}
requests.post(link, files=file)
