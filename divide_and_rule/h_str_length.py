class StrLengthThread(threading.Thread):
    def __init__(self, word):
        if type(word) is not str:
            raise Exception("word is not a string")
        else:
            self.__word = word
