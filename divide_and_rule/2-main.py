from h_reverse_str import ReverseStrThread

text = '''In computer science, a thread of execution is the smallest sequence of programmed instructions that can be managed independently by a scheduler, which is typically a part of the operating system.'''

words = text.split(" ")
reverse_str_threads = []

for word in words:
    reverse_str_thread = ReverseStrThread(word)
    reverse_str_threads += [reverse_str_thread]
    reverse_str_thread.start()

for t in reverse_str_threads:
    t.join()

print "%s" % ReverseStrThread.sentence
