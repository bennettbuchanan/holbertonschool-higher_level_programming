# from task_model import TaskModel
# from task_view import TaskView
import Tkinter as tk
from task_model import TaskModel
from task_view import TaskView

root = tk.Tk()
root.withdraw()
tv = TaskView(root)
tv.update_title("Finish this funny project")
root.mainloop()


# from Tkinter import *
#
# root = Tk()
#
# var = StringVar()
# label = Label( root, textvariable=var, relief=RAISED )
#
# var.set("Hey!? How are you doing?")
# label.pack()
# root.mainloop()
