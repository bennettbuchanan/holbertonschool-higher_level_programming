"""Class"""
class TaskModel(object):
    def __init__(self, title):
        """This is a class of TaskModel.

        Keyword arguments:
        title -- A string with at least one char as parameter.
        """
        if len(title) == 0 or type(title) != str:
            raise Exception("title is not a string")
        self.__title = title

    def __callback_title(self):
        """Function that has been set. Otherwise this has no body."""
        pass

    def set_callback_title(self, func):
        """Takes a function as a parameter and sets callback_title() to
        that function.
        """
        self.__callback_title = func

    def get_title(self):
        """Return private title attribute."""
        return self.__title

    def toggle(self):
        """Redifine private attribute title as a reversed string. Call the
        function callback_title() with the new title as parameter.
        """
        self.__title = self.__title[::-1]
        self.__callback_title(self.__title)

    def __str__(self):
        """Return the title in quotes, and the satus of whether or not toggle()
        has been called on the title.
        """
        return self.__title
