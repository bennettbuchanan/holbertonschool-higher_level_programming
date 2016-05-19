from family import Person

p = Person(1, "Julien", [12, 24, 1980], "Male", "Blue")
p.last_name = "Dupont"
print "%s has %d years old" % (p, p.age())

p2 = Person(2, "Marc", [2, 4, 1986], "Male", "Green")
p2.last_name = "Zuckerberg"

if p > p2:
    print "%s is older than %s" % (p, p2)
else:
    print "%s is younger than %s" % (p, p2)
