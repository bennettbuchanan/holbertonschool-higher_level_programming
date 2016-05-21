import json
"""Used for verifying a file's existence."""
import os.path

"""Class of Person"""
class Person(object):
    """A class of person. This Person must have either Blue, Green or Brown
    eyes and be either a Female of Male. Returns a string that is the
    concatenated first_name and last_name of the person with a space in
    between.

    Keyword arguments:
        id -- A unique id for the Person instance.
        first_name -- The first name of the Person.
        date_of_birth -- The date of birth of the Person. Takes the form of
        list of three integers: date_of_birth[0] is month date_of_birth[1] is
        day, date_of_birth[2] is year.
        genre -- The sex of the Person.
        eyes_color -- The eye color of the Person.
    """
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        """Set all attibutes as private and test for validity."""
        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")
        self.__id = id

        if type(first_name) is not str or len(first_name) is 0:
            raise Exception("string is not a string")
        self.__first_name = first_name

        """
        Test to ensure user has entered a list of three integers for
        date_of_birth attribute. Also, test to ensure that the months and
        days are within a valid range.
        """
        j = 0
        if type(date_of_birth) is not list:
            raise Exception("date_of_birth is not a valid date")
        for n in date_of_birth:
            if type(n) is not int:
                raise Exception("date_of_birth is not a valid date")
            j = j + 1
        if j != 3:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] < 1 or date_of_birth[0] > 12:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] < 1 or date_of_birth[1] > 31:
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth

        if genre not in Person.GENRES or type(genre) is not str:
            raise Exception("genre is not valid")
        self.__genre = genre

        if eyes_color not in Person.EYES_COLORS or type(eyes_color) is not str:
            raise exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

        """Add an empty array to enable testing for whether the Person has
        children."""
        self.children = []

    """Setter."""
    def just_married_with(self):
        return self.__id

    """Getter of id, eyes_color, genre, date_of_birth, and first_name."""

    def get_id(self):
        """Return the unique id of the Person."""
        return self.__id

    def get_eyes_color(self):
        """Return the eye color of the Person."""
        return self.__eyes_color

    def get_genre(self):
        """Return the sex of the Person."""
        return self.__genre

    def get_date_of_birth(self):
        """Return the date of birth of the Person."""
        return self.__date_of_birth

    def get_first_name(self):
        """Return the first name of the Person."""
        return self.__first_name

    """Additional functions of Person class."""

    def is_male(self):
        """Return True if Person is Male, and False otherwise."""
        if self.__genre is "Male":
            return True
        else:
            return False

    def age(self):
        """
        Return the current age (in years) based on date_of_birth and
        the date 05/20/2016.
        """
        date = [5, 20, 2016]
        if self.__date_of_birth[0] >= date[0]:
            if self.__date_of_birth[1] > date[1]:
                return date[2] - (self.__date_of_birth[2] + 1)
            else:
                return date[2] - self.__date_of_birth[2]
        else:
            return date[2] - self.__date_of_birth[2]

    def json(self):
        """
        Return a Hash describing the person by these keys: id, eyes_color,
        genre, date_of_birth, first_name, last_name.
        """
        desc = {
        'id' : self.__id,
        'eyes_color' : self.__eyes_color,
        'genre' : self.__genre,
        'date_of_birth' : self.__date_of_birth,
        'first_name' : self.__first_name,
        }

        """
        If the Class does not have an attribute of last_name, assign 'unknwon'
        to the dict desc.
        """
        if hasattr(self, 'last_name'):
            desc['last_name'] = self.last_name
        else:
            desc['last_name'] = "unknown"

        """If the person is not married, set their status to zero. Otherwise
        set it to the id of the person they are married to.
        """
        if hasattr(self, 'is_married_to'):
            desc['is_married_to'] = self.is_married_to
        else:
            desc['is_married_to'] = "0"
        return desc

    def load_from_json(self, json):
        """Assign Person attributes based on json dict."""
        if type(json) != dict:
            Exception("json is not valid")
        """
        Loop through the json object, if a Person attribute is found,
        update it based on its corresponding value in the json object.
        """
        for k in json:
            if k == "id":
                self.__id = json[k]
            if k == "first_name":
                self.__first_name = json[k]
            if k == "date_of_birth":
                self.__date_of_birth = json[k]
            if k == "day":
                self.__day = json[k]
            if k == "genre":
                self.__genre = json[k]
            if k == "eyes_color":
                self.__eyes_color = json[k]
            if k == "is_married_to":
                self.is_married_to = json[k]
            if k == "last_name":
                self.last_name = json[k]

    def is_married(self):
        """Check to see if attribute is_married_to does not equal zero. If it
        is zero, then the person is not married. Otherwise, the value will be
        the id of the person they are married to.
        """
        if self.is_married_to == 0:
            return False
        else:
            return True

    def just_married_with(self, p):
        """Assign attribute is_married_to with the id of the person p. and
        vice versa, such that they are connected by id numbers."""
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if self.can_be_married() == False or p.can_be_married() == False:
            raise Exception("Can't be married")

        self.is_married_to = p.__id
        p.is_married_to = self.__id
        if p.__genre == "Female":
            p.last_name = self.last_name
        if self.__genre == "Female":
            self.last_name = p.last_name

    """Overloading methods for comparison operations."""

    def __gt__(self, other):
        """Return True if this Person is older than the other Person."""
        return self.age() > other.age()

    def __ge__(self, other):
        """
        Return True if this Person is older than the other Person or the same
        age as them.
        """
        return self.age() >= other.age()

    def __lt__(self, other):
        """Return True if this Person is younger than the other Person."""
        return self.age() < other.age()

    def __le__(self, other):
        """
        Return True if this Person is younger than the other Person or is
        same age as them.
        """
        return self.age() <= other.age()

    def __eq__(self, other):
        """Return True if this Person is the same age as the other Person."""
        return self.age() == other.age()

    def __str__(self):
        """Return the full name of the Person."""
        return self.__first_name + " " + self.last_name

"""Subclasses of Person."""

class Baby(Person):
    """A sublass of Person.

    Keyword arguments:

    """
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        """Tests for validity of function attributes. Returns a Baby object
        with the attributes passed as parameters. The function also assigns
        a list of ids (the first being the id of the instance p, and the second
        the id passed as paremeter) to a public attribute children of self
        (i.e., self.children). If either self or p is not an instance of an
        Adult object, then raise an exception.

        Keyword arguments:
        p -- The person instance that this Person had a child with.
        id -- The id of the Baby object.
        first_name -- The first name of the Baby object.
        date_of_birth --  The date of birth of the Baby. Takes the form of
        list of three integers: date_of_birth[0] is month date_of_birth[1] is
        day, date_of_birth[2] is year.
        genre -- The gender of the Baby.
        eyes_color -- The eye color of the Baby.
        """

        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")

        if type(first_name) is not str or len(first_name) is 0:
            raise Exception("string is not a string")

        """
        Test to ensure user has entered a list of three integers for
        date_of_birth attribute. Also, test to ensure that the months and
        days are within a valid range.
        """
        j = 0
        if type(date_of_birth) is not list:
            raise Exception("date_of_birth is not a valid date")
        for n in date_of_birth:
            if type(n) is not int:
                raise Exception("date_of_birth is not a valid date")
            j = j + 1
        if j != 3:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] < 1 or date_of_birth[0] > 12:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] < 1 or date_of_birth[1] > 31:
            raise Exception("date_of_birth is not a valid date")

        if genre not in Person.GENRES or type(genre) is not str:
            raise Exception("genre is not valid")

        if eyes_color not in Person.EYES_COLORS or type(eyes_color) is not str:
            raise exception("eyes_color is not valid")

        if type(p) == None:
            raise Exception("p is not an Adult of Senior")

        if type(p) != Adult:
            if type(p) != Senior:
                raise Exception("p is not an Adult of Senior")

        if p.can_have_child() == False or self.can_have_child() == False:
            raise Exception("Can't have baby")

        """Assign a list of ids to the public attribute of self."""
        self.children = [id, p.get_id()]

        return Baby(id, first_name, date_of_birth, genre, eyes_color)

    def adopt_child(self, c):
        """Determine whether self can have a child. If so, append c instance
        into the array of children ids.
        """
        if self.can_have_child() != True:
            raise Exception("Can't adopt child")

        self.children.append(c.get_id())
        
    def need_help(self):
        """Returns True for this subclass."""
        return True
    def is_young(self):
        """Returns True for this subclass."""
        return True
    def can_run(self):
        """Returns False for this subclass."""
        return False
    def can_vote(self):
        """Returns False for this subclass."""
        return False
    def can_be_married(self):
        """Returns False for this subclass."""
        return False
    def can_have_child(self):
        """Returns False for this subclass."""
        return False

class Teenager(Person):
    """A sublass of Person.

    Keyword arguments:

    """
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        """Tests for validity of function attributes. Returns a Baby object
        with the attributes passed as parameters. The function also assigns
        a list of ids (the first being the id of the instance p, and the second
        the id passed as paremeter) to a public attribute children of self
        (i.e., self.children). If either self or p is not an instance of an
        Adult object, then raise an exception.

        Keyword arguments:
        p -- The person instance that this Person had a child with.
        id -- The id of the Baby object.
        first_name -- The first name of the Baby object.
        date_of_birth --  The date of birth of the Baby. Takes the form of
        list of three integers: date_of_birth[0] is month date_of_birth[1] is
        day, date_of_birth[2] is year.
        genre -- The gender of the Baby.
        eyes_color -- The eye color of the Baby.
        """

        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")

        if type(first_name) is not str or len(first_name) is 0:
            raise Exception("string is not a string")

        """
        Test to ensure user has entered a list of three integers for
        date_of_birth attribute. Also, test to ensure that the months and
        days are within a valid range.
        """
        j = 0
        if type(date_of_birth) is not list:
            raise Exception("date_of_birth is not a valid date")
        for n in date_of_birth:
            if type(n) is not int:
                raise Exception("date_of_birth is not a valid date")
            j = j + 1
        if j != 3:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] < 1 or date_of_birth[0] > 12:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] < 1 or date_of_birth[1] > 31:
            raise Exception("date_of_birth is not a valid date")

        if genre not in Person.GENRES or type(genre) is not str:
            raise Exception("genre is not valid")

        if eyes_color not in Person.EYES_COLORS or type(eyes_color) is not str:
            raise exception("eyes_color is not valid")

        if type(p) == None:
            raise Exception("p is not an Adult of Senior")

        if type(p) != Adult:
            if type(p) != Senior:
                raise Exception("p is not an Adult of Senior")

        if p.can_have_child() == False or self.can_have_child() == False:
            raise Exception("Can't have baby")

        """Assign a list of ids to the public attribute of self."""
        self.children = [id, p.get_id()]

        return Baby(id, first_name, date_of_birth, genre, eyes_color)

    def adopt_child(self, c):
        """Determine whether self can have a child. If so, append c instance
        into the array of children ids.
        """
        if self.can_have_child() != True:
            raise Exception("Can't adopt child")

        self.children.append(c.get_id())

    def can_run(self):
        """Returns True for this subclass."""
        return True
    def is_young(self):
        """Returns True for this subclass."""
        return True
    def need_help(self):
        """Returns False for this subclass."""
        return False
    def can_vote(self):
        """Returns False for this subclass."""
        return False
    def can_be_married(self):
        """Returns False for this subclass."""
        return False
    def can_have_child(self):
        """Returns False for this subclass."""
        return False

class Adult(Person):
    """A sublass of Person.

    Keyword arguments:

    """
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        """Tests for validity of function attributes. Returns a Baby object
        with the attributes passed as parameters. The function also assigns
        a list of ids (the first being the id of the instance p, and the second
        the id passed as paremeter) to a public attribute children of self
        (i.e., self.children). If either self or p is not an instance of an
        Adult object, then raise an exception.

        Keyword arguments:
        p -- The person instance that this Person had a child with.
        id -- The id of the Baby object.
        first_name -- The first name of the Baby object.
        date_of_birth --  The date of birth of the Baby. Takes the form of
        list of three integers: date_of_birth[0] is month date_of_birth[1] is
        day, date_of_birth[2] is year.
        genre -- The gender of the Baby.
        eyes_color -- The eye color of the Baby.
        """

        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")

        if type(first_name) is not str or len(first_name) is 0:
            raise Exception("string is not a string")

        """
        Test to ensure user has entered a list of three integers for
        date_of_birth attribute. Also, test to ensure that the months and
        days are within a valid range.
        """
        j = 0
        if type(date_of_birth) is not list:
            raise Exception("date_of_birth is not a valid date")
        for n in date_of_birth:
            if type(n) is not int:
                raise Exception("date_of_birth is not a valid date")
            j = j + 1
        if j != 3:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] < 1 or date_of_birth[0] > 12:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] < 1 or date_of_birth[1] > 31:
            raise Exception("date_of_birth is not a valid date")

        if genre not in Person.GENRES or type(genre) is not str:
            raise Exception("genre is not valid")

        if eyes_color not in Person.EYES_COLORS or type(eyes_color) is not str:
            raise exception("eyes_color is not valid")

        if type(p) == None:
            raise Exception("p is not an Adult of Senior")

        if type(p) != Adult:
            if type(p) != Senior:
                raise Exception("p is not an Adult of Senior")

        if p.can_have_child() == False or self.can_have_child() == False:
            raise Exception("Can't have baby")

        """Assign a list of ids to the public attribute of self."""
        self.children = [id, p.get_id()]

        return Baby(id, first_name, date_of_birth, genre, eyes_color)

    def adopt_child(self, c):
        """Determine whether self can have a child. If so, append c instance
        into the array of children ids.
        """
        if self.can_have_child() != True:
            raise Exception("Can't adopt child")

        self.children.append(c.get_id())

    def can_run(self):
        """Returns True for this subclass."""
        return True
    def can_vote(self):
        """Returns True for this subclass."""
        return True
    def can_be_married(self):
        """Returns True for this subclass."""
        return True
    def can_have_child(self):
        """Returns True for this subclass."""
        return True
    def need_help(self):
        """Returns False for this subclass."""
        return False
    def is_young(self):
        """Returns False for this subclass."""
        return False

class Senior(Person):
    """A sublass of Person.

    Keyword arguments:

    """
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        """Tests for validity of function attributes. Returns a Baby object
        with the attributes passed as parameters. The function also assigns
        a list of ids (the first being the id of the instance p, and the second
        the id passed as paremeter) to a public attribute children of self
        (i.e., self.children). If either self or p is not an instance of an
        Adult object, then raise an exception.

        Keyword arguments:
        p -- The person instance that this Person had a child with.
        id -- The id of the Baby object.
        first_name -- The first name of the Baby object.
        date_of_birth --  The date of birth of the Baby. Takes the form of
        list of three integers: date_of_birth[0] is month date_of_birth[1] is
        day, date_of_birth[2] is year.
        genre -- The gender of the Baby.
        eyes_color -- The eye color of the Baby.
        """

        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")

        if type(first_name) is not str or len(first_name) is 0:
            raise Exception("string is not a string")

        """
        Test to ensure user has entered a list of three integers for
        date_of_birth attribute. Also, test to ensure that the months and
        days are within a valid range.
        """
        j = 0
        if type(date_of_birth) is not list:
            raise Exception("date_of_birth is not a valid date")
        for n in date_of_birth:
            if type(n) is not int:
                raise Exception("date_of_birth is not a valid date")
            j = j + 1
        if j != 3:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] < 1 or date_of_birth[0] > 12:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] < 1 or date_of_birth[1] > 31:
            raise Exception("date_of_birth is not a valid date")

        if genre not in Person.GENRES or type(genre) is not str:
            raise Exception("genre is not valid")

        if eyes_color not in Person.EYES_COLORS or type(eyes_color) is not str:
            raise exception("eyes_color is not valid")

        if type(p) == None:
            raise Exception("p is not an Adult of Senior")

        if type(p) != Adult:
            if type(p) != Senior:
                raise Exception("p is not an Adult of Senior")

        if p.can_have_child() == False or self.can_have_child() == False:
            raise Exception("Can't have baby")

        """Assign a list of ids to the public attribute of self."""
        self.children = [id, p.get_id()]

        return Baby(id, first_name, date_of_birth, genre, eyes_color)

    def adopt_child(self, c):
        """Determine whether self can have a child. If so, append c instance
        into the array of children ids.
        """
        if self.can_have_child() != True:
            raise Exception("Can't adopt child")

        self.children.append(c.get_id())

    def need_help(self):
        """Returns True for this subclass."""
        return True
    def can_vote(self):
        """Returns True for this subclass."""
        return True
    def can_be_married(self):
        """Reutnrs True for this subclass."""
        return True
    def is_young(self):
        """Returns False for this subclass."""
        return False
    def can_run(self):
        """Returns False for this subclass."""
        return False
    def can_have_child(self):
        """Returns False for this subclass."""
        return False

def load_from_file(filename):
    """Check for file existence, and if it's found, open a file passed as
    filename and return Person objects (this does not return JSON objects).
    In this way, the JSON objects in the file can be used with methods in the
    Person class and its subclass if applicable.
    """
    if type(filename) != str or os.path.isfile(filename) != True:
        raise Exception("filename is not valid or doesn't exist")
    with open(filename) as json_file:
        data = json.load(json_file)
    json_file.close()

    """Generate an array of Person (or a corresponding subclass) objects from
    JSON objects.
    """
    arr = []
    class_dict = {"Senior": Senior, "Adult": Adult, "Teenager": Teenager, "Baby": Baby}
    for i in range(0, len(data)):
        d = data[i]

        """Loop through array, if the object is a subclass (i.e., it has a key
        of 'kind'), then generate a class with the value of kind (the class
        comes from the class_dict).
        """
        j = 0
        for i in d:
            """If the object has a key of 'kind', then we know this object
            if a subclass of Person. Thus generate an instance with its
            corresponding subclass. Otherwise create a Person instance.
            """
            if i == 'kind':
                p = class_dict[d['kind']](d['id'], str(d['first_name']), d['date_of_birth'], str(d['genre']), str(d['eyes_color']))
                break
            if j + 1 == len(d):
                p = Person(d['id'], str(d['first_name']), d['date_of_birth'], str(d['genre']), str(d['eyes_color']))
            j = j + 1
        j = 0
        for i in d:
            """If the object has a key of 'last_name', then the last name is
            already set. Otherwise we need to set it to an empty string in
            case we want to later turn it into a JSON object.
            """
            if i == 'last_name':
                p.last_name = d['last_name']
                break
            if j + 1 == len(d):
                p.last_name = "unknown"
            j = j + 1
        j = 0
        for i in d:
            """If the object has a key of 'last_name', then the last name is
            already set. Otherwise we need to set it to an empty string in
            case we want to later turn it into a JSON object.
            """
            if i == 'is_married_to':
                p.is_married_to = d['is_married_to']
                break
            if j + 1 == len(d):
                p.is_married_to = 0
            j = j + 1
        arr.append(p)
    return arr

def save_to_file(list, filename):
    """Iterate through a list. If the type is not a dict (meaning it is
    probably an inherited class object), then store the particular subclass
    in var kind. Then append the name of the subclass to the dict. Finally,
    open the filename that was passed as an argument and write the json
    data to the file.
    """
    for i in range(0, len(list)):
        if type(list[i]) != dict:
            kind = type(list[i])
            list[i] = list[i].json()

            list[i]['kind'] = kind.__name__
    target = open(filename, 'w')
    list_dump = json.dumps(list)
    target.write(list_dump)
    target.close()
