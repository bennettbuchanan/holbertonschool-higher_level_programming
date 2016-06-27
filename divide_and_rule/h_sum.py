import threading


class SumThread(threading.Thread):
    def __init__(self, numbers):
        threading.Thread.__init__(self)
        if all(isinstance(i, int) for i in numbers) is False or len(numbers) is 0:
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
        if all(isinstance(i, int) for i in numbers) is False or len(numbers) is 0:
            raise Exception("numbers is not an array of integers")
        else:
            self.__numbers = numbers

        if type(nb_threads) is not int:
            raise Exception("nb_threads is not an integer")
        else:
            self.__nb_threads = nb_threads

        SumThread.sum = 0
        self.__threads = []

        i = 0
        for n in xrange(0, len(self.__numbers), self.__nb_threads):
            if i == 0:
                thread = SumThread(self.__numbers[0:self.__nb_threads])
            else:
                thread = SumThread(self.__numbers[i * self.__nb_threads:(i * self.__nb_threads) + self.__nb_threads])
            self.__threads += [thread]
            thread.start()
            i += 1


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
