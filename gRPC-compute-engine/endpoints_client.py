import grpc
import endpoints_pb2_grpc
import endpoints_pb2



class UsersClient():
    '''
    Client to execute the requests
    '''
    def __init__(self):
        self.host = "127.0.0.1"
        #self.host= "35.203.149.138"
        self.port = 80

        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))

        self.stub = endpoints_pb2_grpc.UsersStub(self.channel)

    def get_users(self, message=None):
        entity_to_get = endpoints_pb2.Entity(entity="None")
        response = self.stub.GetUsers(entity_to_get)
        return response

    def get_user(self, message="joangro"):
        user_to_get = endpoints_pb2.User(username=message)
        response = self.stub.getUser(user_to_get)
        return response

client = UsersClient()
print(client.get_users())
print(client.get_user())
