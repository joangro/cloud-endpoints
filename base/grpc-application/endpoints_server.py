import grpc
import api_pb2_grpc
import api_pb2

from google.cloud import datastore
from concurrent import futures

class UsersServicer(api_pb2_grpc.UsersServicer):
    def __init__(self, *args, **kwargs):
        self.server_port = 8080

    def GetUsers(self, request, context):
        # request should be empty
        client = DatastoreClient()
        query = client.query(kind='Stack-user')
        user = list(query.fetch())[0]
        print(user)
        result = {'users': user}
        return api_pb2.StackUsers(**result)

    def start_server(self):
        endpoints_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        endpoints_server.add_insecure_port('[::]:{}'.format(self.server_port))

        endpoints_server.start()

        print("Endpoints server started")
        try:
            while True:
                import time
                time.sleep(200)
        except KeyboardInterrupt:
            endpoints_service.stop(0)
            print("Endpoints server stopped")






def DatastoreClient():
    return datastore.Client(
                project="wave16-joan"
            )



server = UsersServicer()
server.start_server()
