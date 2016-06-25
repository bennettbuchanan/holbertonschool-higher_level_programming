import threading
import time
import random


class FibonacciThread(threading.Thread):
    def __init__(self, number):
        '''Computes the fibonnacci number on a new thread.

        Keyword arguments:
        number -- The number to find the corresponding fibonnacci number.
        '''
        threading.Thread.__init__(self)
        if type(number) is not int:
            raise Exception("number is not an integer")
        else:
            self.__number = number

    def run(self):
        '''Set the run() method for this thread's activity.'''
        time.sleep(random.uniform(1, 3))
        fibo = self.__number
        tmp = 1
        tmp_1 = 1

        if fibo > 0 and fibo < 3:
            fibo = 1
        else:
            for x in range(fibo - 2):
                fibo = tmp + tmp_1
                tmp = fibo - tmp
                tmp_1 = fibo

        print str(self.__number) + " => " + str(fibo)
