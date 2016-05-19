"""Class of Person"""
class Person(object):
    """A person. This Person must have either Blue, Green or Brown eyes and
    be either a Female of Male. Returns a string that is the concatenated
    first_name and last_name of the person with a space in between.

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

    """Additional functions."""

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
        return 2016 - self.__date_of_birth[2]

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
