# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import endpoints_pb2 as endpoints__pb2


class UsersStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetUsers = channel.unary_unary(
        '/endpoints.Users/GetUsers',
        request_serializer=endpoints__pb2.Entity.SerializeToString,
        response_deserializer=endpoints__pb2.UserList.FromString,
        )
    self.getUser = channel.unary_unary(
        '/endpoints.Users/getUser',
        request_serializer=endpoints__pb2.User.SerializeToString,
        response_deserializer=endpoints__pb2.UserReturned.FromString,
        )


class UsersServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetUsers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetUsers': grpc.unary_unary_rpc_method_handler(
          servicer.GetUsers,
          request_deserializer=endpoints__pb2.Entity.FromString,
          response_serializer=endpoints__pb2.UserList.SerializeToString,
      ),
      'getUser': grpc.unary_unary_rpc_method_handler(
          servicer.getUser,
          request_deserializer=endpoints__pb2.User.FromString,
          response_serializer=endpoints__pb2.UserReturned.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'endpoints.Users', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))