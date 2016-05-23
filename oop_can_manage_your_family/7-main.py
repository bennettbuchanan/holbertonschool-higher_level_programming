from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

my_family = load_from_file("my_family.json")

marc = my_family[0]
parents = marc.who_are_my_parents(my_family)

print "My parents are %s" % (", ".join(map(str, parents)))

save_to_file(my_family, "my_family.json")
