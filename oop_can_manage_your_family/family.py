import json
import itertools

def load_from_file(filename):
    """Open a file passed as filename and return json data objects."""
    with open(filename) as json_file:
        data = json.load(json_file)
    json_file.close()
    return data

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
        date_of_birth attribute.
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
        self.__date_of_birth = date_of_birth

        if genre not in Person.GENRES or type(genre) is not str:
            raise Exception("genre is not valid")
        self.__genre = genre

        if eyes_color not in Person.EYES_COLORS or type(eyes_color) is not str:
            raise exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

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
        'last_name' : self.last_name
        }
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

    """Overloading methods for comparison operations."""

    def __gt__(self, other):
        """Return True if this Person is older than the other Person."""
        return 2016 - self.__date_of_birth[2] > 2016 - other.__date_of_birth[2]

    def __ge__(self, other):
        """
        Return True if this Person is older than the other Person or the same
        age as them.
        """
        return 2016 - self.__date_of_birth[2] >= 2016 - other.__date_of_birth[2]

    def __lt__(self, other):
        """Return True if this Person is younger than the other Person."""
        return 2016 - self.__date_of_birth[2] < 2016 - other.__date_of_birth[2]

    def __le__(self, other):
        """
        Return True if this Person is younger than the other Person or is
        same age as them.
        """
        return 2016 - self.__date_of_birth[2] <= 2016 - other.__date_of_birth[2]

    def __eq__(self, other):
        """Return True if this Person is the same age as the other Person."""
        return 2016 - self.__date_of_birth[2] == 2016 - other.__date_of_birth[2]

    def __str__(self):
        """Return the full name of the Person."""
        return self.__first_name + " " + self.last_name

"""Subclasses of Person."""

class Baby(Person):
    """A sublass of Person.

    Keyword arguments:

    """
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

class Teenager(Person):
    """A sublass of Person.

    Keyword arguments:

    """
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

class Adult(Person):
    """A sublass of Person.

    Keyword arguments:

    """
    def can_run(self):
        """Returns True for this subclass."""
        return True
    def can_vote(self):
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
    def need_help(self):
        """Returns True for this subclass."""
        return True
    def can_vote(self):
        """Returns True for this subclass."""
        return True
    def is_young(self):
        """Returns False for this subclass."""
        return False
    def can_run(self):
        """Returns False for this subclass."""
        return True
