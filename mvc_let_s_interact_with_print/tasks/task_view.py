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

        self.__title_var = tk.StringVar()
        self.__title_label = tk.Label(self, textvariable = self.__title_var)
        self.__title_label.pack(side = RIGHT, padx = 5, pady = 5)

        self.toggle_button = tk.Button(self, text = "Reverse", width = 10)
        self.toggle_button.pack(side = LEFT, padx = 5, pady = 5)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(side = BOTTOM, padx = 5, pady = 5)

        self.e = Entry(self)
        self.e.pack()
        self.e.focus_set()

        self.add_button = Button(self, text="add item", width=10)
        self.add_button.pack()

        self.remove_button = Button(self, text="remove item", width=10)
        self.remove_button.pack()

    def insert(self, item):
        """Insert an item in the list."""
        self.listbox.insert(END, item)

    def delete(self, item):
        """Remove everything between the item and then end of the list."""
        self.listbox.delete(item, END)

    def update_title(self, title):
        """Set the initial title value, and callback and label.

        Keyword arguments:
        title -- The title to be set in the Label.
        """
        if type(title) != str:
            raise Exception("title is not a string")

        self.__title_var.set(title)
