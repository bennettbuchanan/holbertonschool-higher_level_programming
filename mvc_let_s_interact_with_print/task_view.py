import Tkinter as tk
from Tkinter import *

"""Class"""
class TaskView(tk.Toplevel):
    """Close the root Tk() task window, and create a Toplevel window.

    Keyword arguments:
    master -- The widget master.
    """
    def update_title(self, title):
        label = Label(self.__master, textvariable=self.__title_var)
        self.__title_var.set(title)
        label.pack()

    def toggle_button(self):
        button = Button(self.__master, text="OK", command=callback)
        button.pack()

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.__master = master.deiconify()
        self.__title_var = StringVar()
        self.__title_label = Label()
        button = Button(self.__master, text="OK", command=self.update_title)
        button.pack()


        # self.__textvariable = self.__title_var
        #
        # self.toggle_button
        # def update_title(self, title):
        #     return
