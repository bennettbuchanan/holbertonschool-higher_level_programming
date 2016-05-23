from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file, display

my_family = load_from_file("my_family.json")

display(my_family)
'''
my_family:
- Barbara Coldin is the mother of Monica Dupont (born Coldin but married with Tony Dupont)
- Monica and Tony Dupont have 1 girl: Sonia
- Emilie and Bob Foto have 3 boys: Chris, Marc and Greg
- Sonia is married with Chris and have 1 girl Sophie and 1 boy Alex
'''
