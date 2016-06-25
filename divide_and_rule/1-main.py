from h_str_length import StrLengthThread

text = '''In computer science, a thread of execution is the smallest sequence of programmed
    instructions that can be managed independently by a scheduler, which is typically a part
    of the operating system. The implementation of threads and processes differs between
    operating systems, but in most cases a thread is a component of a process.
    Multiple threads can exist within one process, executing concurrently and sharing
    resources such as memory, while different processes do not share these resources.
    In particular, the threads of a process share its executable code and the values of
    its variables at any given time.'''

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
