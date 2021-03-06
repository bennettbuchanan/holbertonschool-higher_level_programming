import Tkinter as tk
from task_model import TaskModel
from task_view import TaskView

"""Class"""
class TaskController():
    """Links all callbacks from model to update view and links the button of
    view to update model.

    Keyword arguments:
    master -- A Tk constructor.
    model -- A TaskModel class.
    """
    def __init__(self, master, model):

        if isinstance(master, tk.Tk) == False:
            raise Exception("master is not a tk.Tk()")
        if isinstance(model, TaskModel) == False:
            raise Exception("model is not a TaskModel")

        self.__model = model
        self.__view = TaskView(master)
        self.__view.update_title(self.__model.get_title())

        self.__model.set_callback_title(self.callback)
        self.__view.toggle_button.config(command=self.__model.toggle)

    def callback(self, value):
        """Set the callback of the model to return updated title to View."""
        self.__view.update_title(self.__model.get_title())
        return value
