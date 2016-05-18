from square import Square

s = Square(20)
s.set_center([0, 0])
s.set_color("Yellow")
s.name = "Hally"
print "Area of %s is %d" % (s.name, s.area())
print s