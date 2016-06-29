import thread
import datetime
from h_store import Store

my_store = Store(10, 3)

def emulate_people(idx):
    my_store.enter()
    print "%d is in at %s!" % (idx, datetime.datetime.now().strftime("%M:%S"))
    if my_store.buy():
        print "%d has one item at %s!" % (idx, datetime.datetime.now().strftime("%M:%S"))
    else:
        print "No more item for %d at %s" % (idx, datetime.datetime.now().strftime("%M:%S"))

for idx_people in range(0, 15):
    thread.start_new_thread( emulate_people, (idx_people, ) )

while True:
    pass
