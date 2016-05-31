import json
"""Used for verifying a file's existence."""
import os.path

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

    def add_item(self, task):
        """Take an item to append to the list. Add that item to the file."""
        id = len(self.load_from_file('task.json'))
        new_item_hash = self.jsonify(id, task)
        list = []
        for i in self.load_from_file('task.json'):
            list.append(self.jsonify(i['id'], i['task']))
        list.append(new_item_hash)
        self.save_to_file(list, 'task.json')

    def remove_item(self):
        """Take an item to append to the list. Add that item to the file."""
        obj = json.load(open("task.json"))
        for i in xrange(len(obj)):
            if obj[i]['id'] == (len(obj) - 1):
                obj.pop(i)
                break
        open("task.json", "w").write(
            json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
        )

    def jsonify(self, id, task):
        """
        Return a Hash describing the list by id and item.
        """
        desc = {
        'id' : id,
        'task' : task
        }
        return desc

    def save_to_file(self, list, filename):
        """Iterate through a list, saving items to file.
        """
        for i in range(0, len(list)):
            if type(list[i]) != dict:
                kind = type(list[i])
                list[i] = list[i].json()
                list[i]['kind'] = kind.__name__
        target = open(filename, 'w')
        list_dump = json.dumps(list, sort_keys=True, indent=4, separators=(',', ': '))
        target.write(list_dump)
        target.close()

    def load_from_file(self, filename):
        """Return the data from the file to generate a list."""
        if type(filename) != str or os.path.isfile(filename) != True:
            raise Exception("filename is not valid or doesn't exist")
        with open(filename) as json_file:
            data = json.load(json_file)
            return data
        json_file.close()

    def __str__(self):
        """Return the title in quotes, and the satus of whether or not toggle()
        has been called on the title.
        """
        return self.__title
