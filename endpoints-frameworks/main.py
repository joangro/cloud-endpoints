import endpoints
from endpoints import message_types
from endpoints import messages
from endpoints import remote

from google.appengine.ext import ndb


class ReturnUser(messages.Message):
    user = messages.StringField(1)

class ReturnUsers(messages.Message):
    users = messages.MessageField(ReturnUser, 1, repeated=True)

class RequestUser(messages.Message):
    user = messages.StringField(1)

class RequestUsers(messages.Message):
    user = message_types.VoidMessage

USER_RESOURCE=endpoints.ResourceContainer(ReturnUser)

USER_PUT_RESOURCE=endpoints.ResourceContainer(
        RequestUser,
        age=messages.StringField(2))

USERS_RESOURCE=endpoints.ResourceContainer(ReturnUsers)


@endpoints.api(name='users', version='v1')
class UsersAPI(remote.Service):

    @endpoints.method(
        #request
        RequestUsers,
        #response
        ReturnUsers,
        path='users',
        http_method='GET',
        name='getUsers')
    def get_users(self, request):
        entities = User.query_users()
        user_list = [ReturnUser(user=entity.username) for entity in entities]
        return ReturnUsers(users=user_list)


class User(ndb.Model):
    username = ndb.StringProperty()

    @classmethod
    def query_users(cls):
        query = User.query()
        users = query.fetch()
        for user in users:
            print('hi')
        return query
       
api = endpoints.api_server([UsersAPI])
