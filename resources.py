from flask import request
from flask_restful import Resource, fields, marshal_with
from db.dals import TaskDAL
from db.session import get_db_session

task_fields = {
    'id': fields.String,
    'title': fields.String,
    'description': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime,

}


class TaskResource(Resource):
    @marshal_with(task_fields)
    def get(self, task_id):
        session = get_db_session()
        try:
            dal = TaskDAL(session)
            task = dal.get_task(task_id)
            if task:
                session.expunge(task)
                return task
            else:
                return {'message': 'Task not found'}, 404
        finally:
            session.close()

    @marshal_with(task_fields)
    def post(self):
        session = get_db_session()
        try:
            data = request.get_json()
            dal = TaskDAL(session)
            task = dal.create_task(title=data['title'], description=data['description'])
            session.expunge(task)
            return task, 201
        finally:
            session.close()

    @marshal_with(task_fields)
    def put(self, task_id):
        session = get_db_session()
        try:
            data = request.get_json()
            dal = TaskDAL(session)
            task = dal.update_task(task_id, title=data['title'], description=data['description'])
            if task:
                session.expunge(task)
                return task
            else:
                return {'message': 'Task not found'}, 404
        finally:
            session.close()

    def delete(self, task_id):
        session = get_db_session()
        try:
            dal = TaskDAL(session)
            success = dal.delete_task(task_id)
            if success:
                return {'message': 'Task deleted'}, 200
            else:
                return {'message': 'Task not found'}, 404
        finally:
            session.close()


class TaskListResource(Resource):
    @marshal_with(task_fields)
    def get(self):
        session = get_db_session()
        try:
            dal = TaskDAL(session)
            tasks = dal.get_all_tasks()
            for task in tasks:
                session.expunge(task)
            return tasks
        finally:
            session.close()

    @marshal_with(task_fields)
    def post(self):
        session = get_db_session()
        try:
            data = request.get_json()
            dal = TaskDAL(session)
            task = dal.create_task(title=data['title'], description=data['description'])
            session.expunge(task)
            return task, 201
        finally:
            session.close()




