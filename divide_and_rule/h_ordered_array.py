import threading


class OrderedArrayThread(threading.Thread):
    '''The OrderedArrayThread, inereting the Thread class. Takes a number as
    parameter and inserts it into its attribute `list` at the appropriate
    location.

    Keyword arguments:
    number -- The ineger to insert into the list.
    '''
    def __init__(self, number):
        threading.Thread.__init__(self)
        if type(number) is not int:
            raise Exception("number is not an integer")
        else:
            self.__number = number

    list = []

    def run(self):
        '''The thread's activity. Determines the location to insert an item in
        an array.
        '''
        i = 0
        for n in OrderedArrayThread.list:
            if n < self.__number:
                i += 1
        OrderedArrayThread.list.insert(i, self.__number)


class OrderedArray(object):
    '''Sorts an array of integers within the array `oa`.

    Keyword arguments:
    number -- An integer to be added to the array `oa`.
    '''
    def __init__(self):
        self.__list = []
        self.__threads = []

    def add(self, number):
        '''Instantiates a thread with the OrderedArrayThread class, adds it to
        the threads list and starts the thread.
        '''
        if type(number) is not int:
            raise Exception("number is not an integer")
        else:
            thread = OrderedArrayThread(number)
            self.__threads += [thread]
            thread.start()

    def isSorting(self):
        '''Determines whether all the threads in the threads list have finished
        execution. Returns True if a thread has not completed, and False
        otherwise.
        '''
        for t in self.__threads:
            if t.is_alive() is True:
                return True

        return False

    def __str__(self):
        '''Returns the ordered list object as a string.'''
        return str(OrderedArrayThread.list)
