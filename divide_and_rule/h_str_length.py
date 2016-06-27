import threading


class StrLengthThread(threading.Thread):
    '''Starts a thread and adds the class' attribute total_str_length.

    Keyword arguments:
    word -- A string, the length of which will be added to total_str_length.
    '''

    def __init__(self, word):
        threading.Thread.__init__(self)
        if type(word) is not str:
            raise Exception("word is not a string")
        else:
            self.__word = word

    total_str_length = None

    def run(self):
        '''Set the run() method for this thread's activity.'''
        StrLengthThread.total_str_length += len(self.__word)
