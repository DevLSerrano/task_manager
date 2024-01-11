from UI.window import create_window
from models.project.project_model import ProjectModel
from models.enum.status_enum import StatusProgress
from models.task.task_model import TaskModel
import datetime


class App:
    def __init__(self):
        super().__init__()

    data_atual = datetime.date.today()
    myProject = ProjectModel(1, "My Project", "This is my project", StatusProgress.inProgress)
    myProject.add_task(TaskModel(1, "Abrir o programa", "Mostrar em prints que a logica funciona.", StatusProgress.delayed, data_atual, 1))
    print('First Task:')
    myList = myProject.get_in_progress_tasks()
    print(myProject.get_in_progress_tasks()[0].get_name())
    print(myProject.get_in_progress_tasks()[0].get_description())
    print(myProject.get_in_progress_tasks()[0].get_status())
    print(myProject.get_in_progress_tasks()[0].get_deadline())

    print('Now I will change the status of the task to completed')
    myProject.complete_task(1)
    print('New status of the task:')
    print(myProject.get_completed_tasks()[0].get_status())

    create_window()


if __name__ == "__main__":
    app = App()
