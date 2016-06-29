import threading
import requests


class LoripsumThread(threading.Thread):
    '''Class to append text from the url to the given file.

    Keyword arguments:
    filename -- The file in which to append the text.
    '''
    def __init__(self, filename):
        threading.Thread.__init__(self)

        self.__filename = filename

    def run(self):
        '''Define the activity of the class. Open the file passed as parameter,
        fetch the string from the url and append to the data to the file.
        '''
        file = open(self.__filename, 'a')
        r = requests.get('http://loripsum.net/api/1/short')
        file.write(r.text.encode('utf-8'))
        file.close()
