import threading


class SumThread(threading.Thread):
    def __init__(self, numbers):
        '''Creates a new thread and adds the numbers passed as an array to the
        this class' variable `sum`.

        Keyword arguments:
        numbers -- An array of numbers to be added to sum.
        '''
        threading.Thread.__init__(self)
        if all(isinstance(i, int) for i in numbers) is False:
            raise Exception("numbers is not an array of integers")
        else:
            self.__numbers = numbers
    sum = 0

    def run(self):
        '''The thread's activity. Determines the location to insert an item in
        an array.
        '''
        arr_sum = 0
        for n in self.__numbers:
            arr_sum += n
        SumThread.sum += arr_sum


class Sum(object):
    def __init__(self, nb_threads, numbers):
        '''Creates a new thread instance, passing it the array numbers divided
        into equal parts nb_threads.

        Keyword arguments:
        numbers -- An array of numbers to be added.
        nb_threads -- The number of times the array should be divided up and
        a new thread created accordingly to be sum
        '''
        if all(isinstance(i, int) for i in numbers) is False:
            raise Exception("numbers is not an array of integers")
        else:
            self.__numbers = numbers

        if type(nb_threads) is not int:
            raise Exception("nb_threads is not an integer")
        else:
            self.__nb_threads = nb_threads

        SumThread.sum = 0
        self.__threads = []
        self.__chunk = []
        indivisible = False

        if len(self.__numbers) % self.__nb_threads:
            indivisible = True

        slice = len(self.__numbers) / self.__nb_threads
        j = 0
        for i in range(0, self.__nb_threads):
            if i + 1 == self.__nb_threads and indivisible is True:
                self.__chunk = self.__numbers[j:]
            else:
                self.__chunk = self.__numbers[j:j + slice]
            j += slice
            thread = SumThread(self.__chunk)
            self.__threads += [thread]
            thread.start()

    def isComputing(self):
        '''Returns True if any threads are not finished, otherwise returns
        False.
        '''
        for t in self.__threads:
            if t.is_alive() is True:
                return True

        return False

    def __str__(self):
        '''Returns the ordered list object as a string.'''
        return str(SumThread.sum)
