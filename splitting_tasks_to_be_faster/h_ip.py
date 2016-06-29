import threading
import requests
import json


class IPThread(threading.Thread):
    '''Update a callback passed as parameter based from the string of the data
    fetched.

    Keyword arguments:
    ip -- The ip that corresponds to the API.
    callback -- The callback function that updates the Tkinter label.
    '''
    def __init__(self, ip, callback):
        threading.Thread.__init__(self)

        self.__ip = ip
        self.__callback = callback

    def run(self):
        '''Defines the thread's activity. Makes a request to the api with the
        specific ip as a string and updates the callback to pass it that
        string. Prints the values to the console.
        '''
        r = requests.get('https://api.ip2country.info/ip?' + str(self.__ip))
        obj = json.loads(r.text)
        self.__callback(obj.get('countryName').encode('utf-8'))
        print "Search: " + str(self.__ip)
        print "countryName: " + obj.get('countryName').encode('utf-8')
