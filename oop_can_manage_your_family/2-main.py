from family import Person, Baby, Teenager, Adult, Senior

b = Baby(3, "Steeve", [7, 4, 2015], "Male", "Green")
b.last_name = "Rod"


if b.can_vote():
    print "%s can vote" % (b)