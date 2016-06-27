import threading
import sys


class StrLenThread(threading.Thread):
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
        StrLenThread.total_str_length += len(self.__word)

words = sys.argv[1].split(" ")
str_length_threads = []

StrLenThread.total_str_length = len(words) - 1
for word in words:
    str_length_thread = StrLenThread(word)
    str_length_threads += [str_length_thread]
    str_length_thread.start()

for t in str_length_threads:
    t.join()

print "%d" % StrLenThread.total_str_length
