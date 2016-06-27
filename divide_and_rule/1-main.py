from h_str_length import StrLengthThread

text = "Hello Holberton School"

words = text.split(" ")
str_length_threads = []

StrLengthThread.total_str_length = len(words) - 1
for word in words:
    str_length_thread = StrLengthThread(word)
    str_length_threads += [str_length_thread]
    str_length_thread.start()

for t in str_length_threads:
    t.join()

print "%d" % StrLengthThread.total_str_length
