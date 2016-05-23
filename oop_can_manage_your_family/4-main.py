from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

my_family = load_from_file("my_family.json")

marc = my_family[0]
vanessa = my_family[1]

if marc.is_married():
    print "Marc is married"

marc.just_married_with(vanessa)
if marc.is_married():
    print "Marc is NOW married"

save_to_file(my_family, "my_family.json")
