from flask import Flask
import time, date
import pprint
app = Flask(__name__)

@app.route('/projects', methods=['POST', 'GET'])
def projects():
    from google.cloud import resource_manager
    client = resource_manager.Client()
    projects = client.list_projects()
    return '<br /> '.join(e.project_id for e in projects)


@app.route('/blobs', methods=['POST', 'GET'])
def bucket_files()
    from google.cloud import storage
    client = storage.Client()
    bucket = client.get_bucket("buckete")
    blobs = list(bucket.list_blobs())
    return "<br />".join(e.name for e in blobs)

if __name__ == "__main__":
app.run("127.0.0.1", 8080, debug=True)
