from db.models import Task


class TaskDAL:
    """
    Data Access Layer for Task operations.
    """
    def __init__(self, db_session):
        self.db_session = db_session

    def get_task(self, task_id):
        """
        Get a task by ID.
        """
        return self.db_session.query(Task).filter_by(id=task_id).first()

    def get_all_tasks(self):
        """
        Get all tasks.
        """
        return self.db_session.query(Task).all()

    def create_task(self, title, description):
        """
        Create a new task.
        """
        new_task = Task(title=title, description=description)
        self.db_session.add(new_task)
        self.db_session.commit()
        self.db_session.refresh(new_task)  # Ensure the task is refreshed and attached to the session
        return new_task

    def update_task(self, task_id, title, description):
        """
        Update an existing task by ID.
        """
        task = self.db_session.query(Task).filter_by(id=task_id).first()
        if task:
            task.title = title
            task.description = description
            self.db_session.commit()
            self.db_session.refresh(task)  # Ensure the task is refreshed and attached to the session
        return task

    def delete_task(self, task_id):
        """
        Delete a task by ID.
        """
        task = self.db_session.query(Task).filter_by(id=task_id).first()
        if task:
            self.db_session.delete(task)
            self.db_session.commit()
            return True
        return False



