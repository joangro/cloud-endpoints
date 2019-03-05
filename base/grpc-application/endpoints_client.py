import grpc
import api_pb2_grpc
import api_pb2



class EndpointsClient(object):
    def __init__(self):
        self.host='localhost'
        self.server_port = 8080

        self.channel = grpc.insecure_channel('{}.{}'.format(self.host, self.server_port))

        self.stub = api_pb2_grpc.UsersStub(self.channel)

    def get_users(self):
        return self.stub.GetUsers()



client = EndpointsClient()

client.get_users()
