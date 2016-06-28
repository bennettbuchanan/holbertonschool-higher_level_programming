import time
from h_sum import Sum

list = range(0, 1000000)

for i in [1, 2, 6, 10, 20, 40]:
    start = time.time()
    sum = Sum(i, list)
    while sum.isComputing():
        pass
    print "With %d threads: %s in %f seconds" % (i, sum, (time.time() - start))
