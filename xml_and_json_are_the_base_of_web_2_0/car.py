import json

class Car(object):
    def __init__(self, *args, **kwargs):
        """Function description.
        Keyword arguments:
        *args -- A tuple of arguments passed.
        **kwargs -- A dictionary of arguments.
        """

        if len(args) == 0:
            if type(kwargs['name']) is not str or len(kwargs['name']) is 0:
                raise Exception("name is not a string")
            if type(kwargs['brand']) is not str or len(kwargs['brand']) is 0:
                raise Exception("brand is not a string")
            if type(kwargs['nb_doors']) is not int or kwargs['nb_doors'] <= 0:
                raise Exception("nb_doors is not > 0")
            self.__name = kwargs['name']
            self.__brand = kwargs['brand']
            self.__nb_doors = kwargs['nb_doors']
        else:
            if type(args[0]['name']) is not str or len(args[0]['name']) is 0:
                raise Exception("name is not a string")
            if type(args[0]['brand']) is not str or len(args[0]['brand']) is 0:
                raise Exception("brand is not a string")
            if type(args[0]['nb_doors']) is not int or args[0]['nb_doors'] <= 0:
                raise Exception("nb_doors is not > 0")
            self.__name = args[0]['name']
            self.__brand = args[0]['brand']
            self.__nb_doors = args[0]['nb_doors']

    def get_name(self):
        """Return get_name."""
        return self.__name

    def get_brand(self):
        """Return get_brand."""
        return self.__brand

    def get_nb_doors(self):
        """Return get_nb_doors."""
        return self.__nb_doors

    def set_nb_doors(self, number):
        """Update the private attribute nb_doors."""
        if type(number) is not int or number <= 0:
            raise Exception("nb_doors is not > 0")
        self.__nb_doors = number

    def to_hash(self):
        """Return a hash of arguments passed."""
        hash = {
            "name": self.__name,
            "brand": self.__brand,
            "nb_doors": self.__nb_doors
        }
        return hash

    def to_json_string(self):
        """Return a string of the class in JSON format."""
        str = self.to_hash()
        return json.dumps(str)

    def to_xml_node(self, doc):
        """Return an XML DOM element with the attributes and values."""
        carNode = doc.createElement("car")
        carNode.setAttribute("nb_doors", str(self.__nb_doors))
        nameNode = doc.createElement("name")
        carNode.appendChild(nameNode)
        nameNode.appendChild(doc.createCDATASection(self.__name))
        brandNode = doc.createElement("brand")
        carNode.appendChild(brandNode)
        brandNode.appendChild(doc.createTextNode(self.__brand))
        return carNode

    def detailed_xml(self, doc):
        """Return an XML DOM element with the attributes and values."""
        carNode = doc.createElement("car")
        carNode.setAttribute("nb_doors", str(self.__nb_doors))
        carNode.setAttribute("weight", str(1000))
        nameNode = doc.createElement("name")
        carNode.appendChild(nameNode)
        nameNode.appendChild(doc.createCDATASection(self.__name))
        brandNode = doc.createElement("brand")
        carNode.appendChild(brandNode)
        brandNode.appendChild(doc.createCDATASection(u"\u00a9" + self.__brand))
        yearNode = doc.createElement("year")
        yearNode.appendChild(doc.createTextNode("2015"))
        carNode.appendChild(yearNode)
        return carNode

    def to_comma(self):
        """Return the data as a CSV."""
        return self.__name + "," + self.__brand + "," + str(self.__nb_doors) + "\n"

    def __str__(self):
        """Return the attributes of this class."""
        return self.__name + " " + self.__brand + " (" + str(self.__nb_doors) + ")"
