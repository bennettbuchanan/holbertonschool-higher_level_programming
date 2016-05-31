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

        for i in self.__model.load_from_file('task.json'):
            self.__view.insert(i['task'])

        self.__model.set_callback_title(self.callback)
        self.__view.toggle_button.config(command=self.__model.toggle)
        self.__view.add_button.config(command=self.add_item)
        self.__view.remove_button.config(command=self.remove_item)

    def add_item(self):
        """Add the item to the JSON file."""
        self.__model.add_item(self.__view.e.get())
        for i in self.__model.load_from_file('task.json'):
            if i['id'] == (len(self.__model.load_from_file('task.json')) - 1):
                self.__view.insert(i['task'])

    def remove_item(self):
        """Remove the item from the JSON file."""
        self.__model.remove_item()
        if len(self.__model.load_from_file('task.json')) == 0:
            self.__view.delete(0)
        else:
            for i in self.__model.load_from_file('task.json'):
                self.__view.delete(len(self.__model.load_from_file('task.json')))

    def callback(self, value):
        """Set the callback of the model to return updated title to View."""
        self.__view.update_title(self.__model.get_title())
        return value
