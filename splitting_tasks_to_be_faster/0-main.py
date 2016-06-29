import sys
from h_loripsum import LoripsumThread

nb_paragraph = int(sys.argv[1])
filename = sys.argv[2]

threads = []
for i in range(0, nb_paragraph):
    t = LoripsumThread(filename)
    t.start()
    threads += [t]

for t in threads:
    t.join
