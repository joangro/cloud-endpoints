from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from google.cloud import datastore


app = Flask(__name__)

api = Api(app)

def DatastoreClient():
    return datastore.Client(
                project="wave16-joan"
            )

    
class AllStackUsers(Resource):
    def get(self):
        client = DatastoreClient()
        query = client.query(kind='Stack-user')
        users = query.fetch()
        return jsonify({'users': [str(e['username']) for e in users]})

class StackUser(Resource):
    def get(self, user_id):
        client = DatastoreClient()
        query = client.query(kind='Stack-user')
        query.add_filter('username', '=', user_id)
        user = list(query.fetch(1))[0]
        return jsonify({"username": user['username']})

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('age', type=int, required=True, help='REQUIRED: Age of the user to create')
        args = parser.parse_args()
        client=DatastoreClient()
        query = client.query(kind='Stack-user')
        query.add_filter('username', '=', user_id)
        if not list(query.fetch()):
            key = client.key('Stack-user')
            entity = datastore.Entity(key=key)
            entity.update({
                    "username": user_id,
                    "age": args['age']
                })
            client.put(entity)
            return "OK", 201

        return "ERROR: User already exists", 400

    def delete(self, user_id):
        client=DatastoreClient()
        query = client.query(kind='Stack-user')
        query.add_filter('username', '=', user_id)
        query.keys_only()
        user = list(query.fetch())
        if not user:
            return "ERROR: User doesn't exist", 400
        
        try:
            client.delete(user[0].key)
            return "User entity deleted", 200
        except:
            return "User could not be deleted", 500
      
@app.route('/')
def index():
    return "hello world"

api.add_resource(AllStackUsers,'/users')
api.add_resource(StackUser,'/users/<user_id>')


if __name__ == "__main__":
    app.run("127.0.0.1", 8080, debug=True)
