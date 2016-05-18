from circle import Circle

c = Circle(4)
c.set_center([0, 0])
c.set_color("Yellow")

print "Area of %s %sis %f" % (c.get_color(), c.name, c.area())
