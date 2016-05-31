from task_model import TaskModel

def test_callback_title(value):
    print "Toggle changed! \"%s\"" % value

t = TaskModel("Finish this funny project")
t.set_callback_title(test_callback_title)
print t
t.toggle()
print t
