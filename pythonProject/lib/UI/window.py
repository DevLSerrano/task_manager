import tkinter as tk

from lib.models.enum.status_enum import StatusProgress
from lib.models.project.project_model import ProjectModel
from lib.models.task.task_model import TaskModel
import datetime


def update_cards(main_frame: tk.Frame, project_list):
    for widget in main_frame.winfo_children():
        widget.destroy()

    for i, project in enumerate(project_list):
        row = (i // 2) + 1
        column = i % 2
        create_card(main_frame, project, row, column)


def create_task_widget(parent: tk.Frame, task: TaskModel):
    task_frame = tk.Frame(parent)
    task_frame.pack(fill="x")

    status_var = tk.BooleanVar()
    status_var.set(task.is_completed())

    def update_color():
        if task.status == StatusProgress.completed:
            color = "green"
        elif task.status == StatusProgress.delayed:
            color = "red" if task.is_completed() else "black"
        else:
            color = "white"
        label.config(fg=color)

    checkbutton = tk.Checkbutton(task_frame, variable=status_var, command=update_color)
    checkbutton.pack(side="left")

    label = tk.Label(task_frame, text=task.description)
    label.pack(side="left", fill="x", expand=True)

    update_color()

    return task_frame


def show_tasks(project: ProjectModel, parent: tk.Frame):
    new_project_window = tk.Toplevel(parent)
    new_project_window.title("Tasks de " + project.get_project_name())
    new_project_window.minsize(600, 400)
    new_project_window.maxsize(800, 800)

    tasks_frame = tk.Frame(new_project_window)
    tasks_frame.pack(fill="both", expand=True)

    for task in project.get_in_progress_tasks():
        create_task_widget(tasks_frame, task)


def add_project(project_list, main_frame: tk.Frame):
    def create_project():
        project_name = name_entry.get()
        project_description = description_entry.get()
        project_list.append(ProjectModel(len(project_list) + 1, project_name, project_description, StatusProgress.inProgress))
        new_project_window.destroy()
        update_cards(main_frame, project_list)

    new_project_window = tk.Toplevel()
    new_project_window.title("Novo Projeto")

    tk.Label(new_project_window, text="Nome do Projeto:").pack()
    name_entry = tk.Entry(new_project_window)
    name_entry.pack()

    tk.Label(new_project_window, text="Descrição do Projeto:").pack()
    description_entry = tk.Entry(new_project_window)
    description_entry.pack()

    add_button = tk.Button(new_project_window, text="Adicionar Projeto", command=create_project)
    add_button.pack()


def create_card(parent: tk.Frame, project: ProjectModel, row: int, column: int):
    card_color = "#33333D"
    text_color = "white"

    card_frame = tk.Frame(parent, bg=card_color, bd=0, )
    card_frame.grid_propagate(False)
    card_frame.grid(row=row, column=column, padx=2, pady=2)

    card_title = tk.Label(card_frame, text=project.get_project_name(), bg=card_color, fg=text_color)
    card_title.pack(padx=10, pady=10)

    see_project_button = tk.Button(
        card_frame,
        text="Visualizar Tasks",
        command=lambda: show_tasks(project, parent),
    )
    see_project_button.pack(pady=20)

    return card_frame


def create_window():
    window = tk.Tk()
    window.title('Task Manager')
    window.minsize(600, 400)
    window.maxsize(800, 800)

    main_frame = tk.Frame(window)
    main_frame.pack(expand=True)

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)

    project_list = [
        ProjectModel(1, "eFolioA", "Projeto nivel 1", StatusProgress.completed, in_progress_tasks=[
            TaskModel(1, "task1", "Descrição task1.", StatusProgress.inProgress, datetime.date.today(), 1),
            TaskModel(2, "task2", "Descrição task2", StatusProgress.completed, datetime.date.today(), 1),
            TaskModel(3, "task3", "Descrição task3", StatusProgress.delayed, datetime.date.today(), 1),
        ]),
        ProjectModel(2, "eFolioB", "Projeto nivel 2", StatusProgress.inProgress),
        ProjectModel(3, "eFolioC", "Projeto nivel 3", StatusProgress.delayed),
    ]

    label = tk.Label(
        main_frame,
        text="Gerenciador de Projetos",
        foreground="white",
    )
    label.pack()

    label.grid(row=0, column=0, columnspan=2)

    row: int = 0
    for i, project in enumerate(project_list):
        row = (i // 2) + 1
        column = i % 2
        create_card(main_frame, project, row, column)
    update_cards(main_frame, project_list)

    button_frame = tk.Frame(window)
    button_frame.pack(expand=True)
    add_project_button = tk.Button(
        button_frame,
        text="Adicionar Projeto",
        command=lambda: add_project(project_list, main_frame)
    )
    add_project_button.grid(row=row + 1, column=0, columnspan=2, pady=20)

    window.mainloop()
