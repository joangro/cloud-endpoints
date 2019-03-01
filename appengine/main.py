from flask import Flask, jsonify
from flask_restful import Resource, Api

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
        return jsonify({
                "username": user['username'],
            })

    def put(self, user_id):
        pass

api.add_resource(AllStackUsers,'/users')
api.add_resource(StackUser,'/users/<user_id>')


if __name__ == "__main__":
    app.run("127.0.0.1", 8080, debug=True)
