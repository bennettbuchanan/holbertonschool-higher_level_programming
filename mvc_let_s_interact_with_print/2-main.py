import Tkinter as tk

from task_model import TaskModel
from task_view import TaskView
from task_controller import TaskController


root = tk.Tk()
root.withdraw()
t = TaskModel("Finish this funny project")
tc = TaskController(root, t)
root.mainloop()
