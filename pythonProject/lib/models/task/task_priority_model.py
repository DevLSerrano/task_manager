from ..task.task_model import TaskModel


class TaskPriority(TaskModel):
    def __init__(self, id, name, description, status, deadline, project_id):
        super().__init__(id, name, description, status, deadline, project_id)
