from task_model import TaskModel
import Tkinter as tk
from Tkinter import *

"""Class"""
class TaskView(tk.Toplevel):
    """Close the root Tk() task window, and create a Toplevel window. This is a
    child class of Toplevel.

    Keyword arguments:
    master -- A Tk constructor.
    """
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)

        if isinstance(master, tk.Tk) == False:
            raise Exception("master is not a tk.Tk()")

        """Ensure widget instances are deleted."""
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        self.toggle_button = Button(self, text = "Reverse", width = 10, command = self.toggle)
        self.toggle_button.pack(side = LEFT, padx = 5, pady = 5)

    def update_title(self, title):
        """Set the initial title value, and callback and label."""
        if type(title) != str:
            raise Exception("title is not a string")

        self.__title_var = StringVar()
        textvariable = self.__title_var
        textvariable.set(title)

        self.__t = TaskModel(textvariable.get())
        self.__t.set_callback_title(self.callback)

        self.__title_label = Label(self, text = self.__t)
        self.__title_label.pack(side = RIGHT, padx = 5, pady = 5)

    def toggle(self):
        """Call the toggle method on the instance t, and updates the label."""
        self.__t.toggle()
        self.__title_label['text'] = self.__t

    def callback(self, value):
        """Set a callback which does nothing, to enable calling toggle()."""
        pass
