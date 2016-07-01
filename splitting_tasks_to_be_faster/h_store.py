from threading import BoundedSemaphore
import time
import random


class Store(object):
    item_number = None
    people_in_store = None

    def __init__(self, item_number, person_capacity):
        '''The store class.

        Keyword arguments:
        item_number -- The number of items that are in the store.
        person_capacity -- The maximum amount of people allowed in the store.
        '''
        self.__item_number = item_number
        self.__person_capacity = person_capacity

        if Store.item_number is None:
            Store.item_number = self.__item_number

        if Store.people_in_store is None:
            Store.people_in_store = BoundedSemaphore(self.__person_capacity)

    def enter(self):
        '''Calls the acquire method on the BoundedSemaphore incrementor.'''
        Store.people_in_store.acquire()
        return

    def buy(self):
        '''Waits between 5 and 10 seconds before calling release on the
        previous acquire. If the items in the store are 0, return False,
        otherwise decrement Store.item_number and return True.
        '''
        time.sleep(random.uniform(5, 10))
        if Store.item_number == 0:
            Store.people_in_store.release()
            return False
        else:
            Store.item_number -= 1
            Store.people_in_store.release()
            return True
