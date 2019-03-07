import endpoints
from endpoints import message_types
from endpoints import messages
from endpoints import remote

from google.appengine.ext import ndb


class ReturnUser(messages.Message):
    user = messages.StringField(1)
    age = messages.StringField(2, required=False)

class ReturnUsers(messages.Message):
    users = messages.MessageField(ReturnUser, 1, repeated=True)

class RequestUser(messages.Message):
    user = messages.StringField(1)

class RequestUsers(messages.Message):
    user = message_types.VoidMessage

class OkStatusResponse(messages.Message):
    status = message_types.VoidMessage

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

    @endpoints.method(
        RequestUser,
        ReturnUser,
        path='users/{user}',
        http_method='GET',
        name='getUser')
    def get_user(self, request):
        queried_user=User.query_user(user=request.user)
        return  ReturnUser(user=queried_user[0].username, age='20')
        
    @endpoints.method(
        # This is actually the request user for this method, reusing message
        ReturnUser,
        OkStatusResponse,
        path='users/{user}',
        http_method='PUT',
        name='addUser')
    def add_user(self, request):
        user_to_add = request.user
        print(user_to_add)
        try:
            user_age = request.age
        except:
            user_age=None
        finally:
        # Create entity
            result = User.create_user(user_to_add, user_age)
            if result == "User exists":
                raise endpoints.BadRequestException("User {} already exists".format(user_to_add))

            return OkStatusResponse()

class User(ndb.Model):
    username = ndb.StringProperty()
    age = ndb.IntegerProperty()

    @classmethod
    def query_users(cls):
        '''
        Query all user under Users entity kind
        '''
        query = User.query()
        users = query.fetch()
        return query

    @classmethod
    def query_user(cls, user):
        '''
        Query a single user from the input, under Users entity kind
        '''
        query=User.query(User.username==user)
        user = query.fetch()
        return user

    @classmethod
    def create_user(cls, user, age=None):
        query = User.query(User.username==user).fetch()
        try:
            # If it succeeds, it means that the user exists
            queried_user = query[0].username
        except IndexError:
            if age is None:
                new_user = User(username=user)
            else:
                new_user = User(username=user, age=int(age))
            new_user.put()
            return "ok"

        return "User exists"
        
    @classmethod
    def delete_user(cls, user):
        pass

       
api = endpoints.api_server([UsersAPI])
