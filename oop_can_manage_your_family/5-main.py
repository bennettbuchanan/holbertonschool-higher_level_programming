from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

my_family = load_from_file("my_family.json")

marc = my_family[0]
vanessa = my_family[1]
boby = my_family[2]

vanessa.adopt_child(boby)
marc.adopt_child(boby)
monica = vanessa.has_child_with(marc, 5, "Monica", [5, 6, 2016], "Female", "Blue")

print "Vanessa has %d children" % (len(vanessa.children))

save_to_file(my_family, "my_family.json")
