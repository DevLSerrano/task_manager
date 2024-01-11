from ..enum.status_enum import StatusProgress
import datetime


class TaskModel:
    def __init__(self, id: int, name: str, description: str, status: StatusProgress, deadline: datetime.date,
                 project_id: int):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.deadline = deadline
        self.project_id = project_id

    def get_name(self) -> str:
        return self.name

    def set_name(self, new_name: str):
        self.name = new_name

    def get_description(self) -> str:
        return self.description

    def set_description(self, new_description: str):
        self.description = new_description

    def get_status(self) -> StatusProgress:
        return self.status

    def set_status(self, new_status: StatusProgress):
        self.status = new_status

    def is_completed(self) -> bool:
        return self.status == StatusProgress.completed
    def is_delayed(self) -> bool:
        return self.status == StatusProgress.delayed

    def get_deadline(self) -> datetime.date:
        return self.deadline

    def set_deadline(self, new_deadline: datetime.date):
        self.deadline = new_deadline

    def get_project_id(self) -> int:
        return self.project_id

    def set_project_id(self, new_project_id: int):
        self.project_id = new_project_id
