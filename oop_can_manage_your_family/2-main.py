from family import Person, Baby, Teenager, Adult, Senior

a = Adult(1, "Marc", [12, 24, 1980], "Male", "Blue")
a.last_name = "Zuckerberg"
b = Baby(3, "Steeve", [7, 4, 2015], "Male", "Green")
b.last_name = "Rod"

if a.can_vote():
    print "%s can vote" % (a)
if b.can_vote():
    print "%s can vote" % (b)
if a.is_young():
    print "%s is young" % (a)
if b.need_help():
    print "%s needs help" % (b)
