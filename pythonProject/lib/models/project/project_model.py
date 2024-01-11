from ..task.task_model import TaskModel
from ..enum.status_enum import StatusProgress


class ProjectModel:
    def __init__(self, project_id: int, project_name: str, project_description: str, project_status: StatusProgress,
                 in_progress_tasks: list[TaskModel] = [], completed_tasks: list[TaskModel] = []):
        self.project_id = project_id
        self.project_name = project_name
        self.project_description = project_description
        self.project_status = project_status
        self.in_progress_tasks = in_progress_tasks
        self.completed_tasks = completed_tasks

    def get_project_name(self) -> str:
        return self.project_name

    def set_project_name(self, new_project_name: str):
        self.project_name = new_project_name

    def get_project_description(self) -> str:
        return self.project_description

    def set_project_description(self, new_project_description: str):
        self.project_description = new_project_description

    def get_project_status(self) -> StatusProgress:
        return self.project_status

    def set_project_status(self, new_project_status: StatusProgress):
        self.project_status = new_project_status

    def get_in_progress_tasks(self) -> list[TaskModel]:
        return self.in_progress_tasks


    def get_completed_tasks(self) -> list[TaskModel]:
        return self.completed_tasks

    def set_completed_tasks(self, new_completed_tasks: list[TaskModel]):
        self.completed_tasks = new_completed_tasks

    def add_task(self, task: TaskModel):
        self.in_progress_tasks.append(task)

    def remove_task(self, task_id: int):
        task = None
        for in_progress_task in self.in_progress_tasks:
            if in_progress_task.id == task_id:
                task = in_progress_task
                break

        if task is not None:
            self.in_progress_tasks.remove(task)

    def complete_task(self, task_id: int):
        task = None
        for in_progress_task in self.in_progress_tasks:
            if in_progress_task.id == task_id:
                task = in_progress_task
                break

        if task is not None:
            task.set_status(StatusProgress.completed)
            self.in_progress_tasks.remove(task)
            self.completed_tasks.append(task)

        if in_progress_task == []:
            self.set_project_status(StatusProgress.completed)
