import grpc
import endpoints_pb2_grpc
import endpoints_pb2



class UsersClient():
    '''
    Client to execute the requests
    '''
    def __init__(self):
        self.host = "127.0.0.1"
        #self.host= "34.76.150.228"
        self.port = 8080

        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))

        self.stub = endpoints_pb2_grpc.UsersStub(self.channel)

    def get_users(self):
        request = endpoints_pb2.EmptyMessage()
        response = self.stub.GetUsers(request)
        return response

    def get_user(self, user="Joan"):
        user_to_get = endpoints_pb2.User(username=user)
        response = self.stub.getUser(user_to_get, metadata=addMetadata())
        return response

    def add_user(self, user="asdasd"):
        user_to_add = endpoints_pb2.User(username=user, age=23)
        response = self.stub.addUser(user_to_add, metadata=addMetadata())
        return response

    def delete_user(self, user="test2"):
        user_to_delete = endpoints_pb2.User(username=user)
        response = self.stub.deleteUser(user_to_delete, metadata=addMetadata())
        return response

def addMetadata(api_key = "AIzaSyCsNkXwvCbqpdmTw7vS-I2YUAa8BS8gg04"):
    metadata = []
    return metadata.append(('x-api-key', api_key))

client = UsersClient()

print(client.get_users())
print(client.get_user(user="Joan"))
print(client.add_user(user="toRemove"))
print(client.delete_user(user="toRemove"))

#print(client.get_user())
