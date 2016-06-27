import time
from h_sum import Sum

# list = range(40, 1000000)
# test = Sum(1, list)
#
# while test.isComputing():
#     pass
# print test
list = range(0, 1000000)

for i in [40]:
    start = time.time()
    sum = Sum(i, list)
    while sum.isComputing():
        pass
    print "With %d threads: %s in %f seconds" % (i, sum, (time.time() - start))
