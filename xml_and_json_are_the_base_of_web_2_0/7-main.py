import urllib
import json
from xml.dom.minidom import Document
from car import Car

"""Load data from the URL and write to a file."""
url = "http://173.246.108.142/oop/cars.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
target = open("7-main.json", 'w')
list_dump = json.dumps(data, sort_keys=True, indent=4,
                       separators=(',', ': '))
target.write(list_dump)
target.close()

with open("7-main.json") as json_file:
    data_file = json.load(json_file)
json_file.close()

i = 0
objArray = []
for obj in data_file:
    c = Car(name=str(obj['name']), brand=str(obj['brand']),
            nb_doors=obj['nb_doors'])
    objArray.append(c)

"""Add the first name to the brandArray, since it must be unique."""
brandArray = [objArray[0].get_brand()]

k = 1
totalDoors = 0
doc = Document()
rootNode = doc.createElement("cars")
"""Traverse the objArray to determine existence in the brandArray."""
for i in objArray:
    for j in brandArray:
        if i.get_brand() == j:
            k = 1
            break
        if k == len(brandArray):
            brandArray.append(i.get_brand())
            k = 1
            break
        k += 1
    totalDoors += i.get_nb_doors()

    carNode = i.detailed_xml(doc)
    rootNode.appendChild(carNode)

doc.appendChild(rootNode)

print doc.toxml(encoding='utf-8')
