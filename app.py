from flask import Flask
from flask_restful import Api
from config import Config
from api.resources import TaskListResource, TaskResource
from api.errors import register_error_handlers

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<string:task_id>')

register_error_handlers(app)

if __name__ == '__main__':
    app.run(debug=True)

