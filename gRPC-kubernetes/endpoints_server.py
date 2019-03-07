import grpc
import endpoints_pb2_grpc
import endpoints_pb2

import time
from google.cloud import datastore
from concurrent import futures

import pprint

class UsersServicer(endpoints_pb2_grpc.UsersServicer):
    '''
    <SERVICE_NAME>Servicer: implements the gRPC server
    '''
    def __init__(self, *args, **kwargs):
        self.server_port = 8080

    def GetUsers(self, request, context):
        '''
        Implements the GetUsers method defined under the Users service. Gets all users from Datastore
        '''
        client = datastore.Client(project="wave16-joan")

        query = client.query(kind='Stack-user')
        users = list(query.fetch())
        
        user_list = endpoints_pb2.UserList()
        
        for user in users:
            user_list.username.append(user['username'])
        
        return user_list

    def getUser(self, request, context):
        '''
        Get a single user from Datastore
        '''
        user_to_get = request.username
        client = datastore.Client(project="wave16-joan")

        query = client.query(kind='Stack-user')
        query.add_filter('username', '=', user_to_get)
        datastore_user = list(query.fetch())[0]
        user = endpoints_pb2.UserReturned(username=datastore_user['username'])
        return user





    def start(self):
        '''
        Starts running the gRPC server
        '''

        endpoints_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # Creates N max asynchronous workers to handle the requests

        endpoints_pb2_grpc.add_UsersServicer_to_server(UsersServicer(), endpoints_server)

        # Where will the server be exposed
        endpoints_server.add_insecure_port('[::]:{}'.format(self.server_port))

        endpoints_server.start()

        try:
            while True:
                time.sleep(3600)

        except KeyboardInterrupt:
            endpoints_server.stop(0)


server = UsersServicer()
server.start()
