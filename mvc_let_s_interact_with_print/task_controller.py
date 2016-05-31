"""Class"""

class TaskController():
    def __init__(self, master, model):

        if isinstance(master, tk.Tk) == False:
            raise Exception("master is not a tk.Tk()")
        if isinstance(model, TaskModel) == False:
            raise Exception("model is not a TaskModel")

        self.__model = model
        self.__view = TaskView(master)
