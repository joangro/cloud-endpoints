from flask import Flask

app = Flask(__name__)

@app.route('/projects', methods=['POST', 'GET'])
def index():
    from google.cloud import resource_manager
    client = resource_manager.Client()
    projects = client.list_projects()
    return '\n'.join(e.project_id for e in projects)


if __name__ == "__main__":
    app.run("127.0.0.1", 8080, debug=True)
