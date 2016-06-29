import threading
import requests
import json
import time
import random


class Store(threading.Thread):
    def __init__(self, item_number, person_capacity):
        threading.Thread.__init__(self)

        self.__item_number = item_number
        self.__person_capacity = person_capacity

    def enter(self):
        if threading.activeCount()

    def buy(self):
        time.sleep(random.uniform(5, 10))
