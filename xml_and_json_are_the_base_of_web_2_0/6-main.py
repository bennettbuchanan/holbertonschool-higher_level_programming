import urllib
import json
from xml.dom.minidom import Document
from car import Car

"""Load data from the URL and write to a file."""
url = "http://173.246.108.142/oop/cars.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
target = open("6-main.json", 'w')
list_dump = json.dumps(data, sort_keys=True, indent=4,
                       separators=(',', ': '))
target.write(list_dump)
target.close()

with open("6-main.json") as json_file:
    data_file = json.load(json_file)
json_file.close()

i = 0
objArray = []
for obj in data_file:
    c = Car(name=str(obj['name']), brand=str(obj['brand']),
            nb_doors=obj['nb_doors'])
    objArray.append(c)

csv_array = []
for i in objArray:
    csv_array.append(i.to_comma())

print "".join(csv_array)
