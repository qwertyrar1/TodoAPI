from flask import Flask
from flask_restx import Api
from config import Config
from api.resources import api as tasks_ns
from api.errors import register_error_handlers

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app, version='1.0', title='My API', description='A simple demonstration API')

api.add_namespace(tasks_ns, path='/tasks')

register_error_handlers(app)

if __name__ == '__main__':
    app.run(debug=True)

