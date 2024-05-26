from flask import Flask
from flask_restful import Api
from config import Config
from resources import TaskListResource, TaskResource

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<string:task_id>')

if __name__ == '__main__':
    app.run(debug=True)

