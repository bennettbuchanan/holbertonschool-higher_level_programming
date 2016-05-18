from circle import Circle

c1 = Circle(4)
c1.set_center([0, 0])
c1.name = "Sun"

c2 = Circle(4)
c2.set_center([1, 1])
c2.name = "Earth"

if c1.intersection(c2):
    print "Intersection between %s and %s" % (c1.name, c2.name)
else:
    print "No intersection between %s and %s" % (c1.name, c2.name)
