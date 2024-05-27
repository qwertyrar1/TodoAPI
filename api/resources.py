from flask import request
from flask_restx import Resource, fields, Namespace
from db.dals import TaskDAL
from db.session import get_db_session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

api = Namespace('tasks', description='Task related operations')

task_fields = api.model('Task', {
    'id': fields.String,
    'title': fields.String,
    'description': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime,
})


class TaskResource(Resource):
    @api.marshal_with(task_fields)
    @api.doc(params={'task_id': 'The task identifier'})
    def get(self, task_id):
        """
        Get a task by ID.
        """
        session = get_db_session()
        try:
            dal = TaskDAL(session)
            task = dal.get_task(task_id)
            if task:
                session.expunge(task)
                return task
            else:
                return {'message': 'Task not found'}, 404
        except NoResultFound:
            return {'message': 'Task not found'}, 404
        except Exception as e:
            return {'message': str(e)}, 500
        finally:
            session.close()

    @api.marshal_with(task_fields)
    @api.expect(task_fields)
    def put(self, task_id):
        """
        Update an existing task by ID.
        """
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
        except NoResultFound:
            return {'message': 'Task not found'}, 404
        except IntegrityError:
            session.rollback()
            return {'message': 'Task with the same ID already exists'}, 400
        except Exception as e:
            return {'message': str(e)}, 500
        finally:
            session.close()

    @api.doc(params={'task_id': 'The task identifier'})
    def delete(self, task_id):
        """
        Delete a task by ID.
        """
        session = get_db_session()
        try:
            dal = TaskDAL(session)
            success = dal.delete_task(task_id)
            if success:
                return {'message': 'Task deleted'}, 200
            else:
                return {'message': 'Task not found'}, 404
        except NoResultFound:
            return {'message': 'Task not found'}, 404
        except Exception as e:
            return {'message': str(e)}, 500
        finally:
            session.close()


class TaskListResource(Resource):
    @api.marshal_with(task_fields)
    def get(self):
        """
        Get all tasks.
        """
        session = get_db_session()
        try:
            dal = TaskDAL(session)
            tasks = dal.get_all_tasks()
            for task in tasks:
                session.expunge(task)
            return tasks
        except Exception as e:
            return {'message': str(e)}, 500
        finally:
            session.close()

    @api.marshal_with(task_fields)
    @api.expect(task_fields)
    def post(self):
        """
        Create a new task in the database.
        """
        session = get_db_session()
        try:
            data = request.get_json()
            dal = TaskDAL(session)
            task = dal.create_task(title=data['title'], description=data['description'])
            session.expunge(task)
            return task, 201
        except IntegrityError:
            session.rollback()
            return {'message': 'Task with the same ID already exists'}, 400
        except Exception as e:
            return {'message': str(e)}, 500
        finally:
            session.close()


api.add_resource(TaskResource, '/<string:task_id>')
api.add_resource(TaskListResource, '/')

