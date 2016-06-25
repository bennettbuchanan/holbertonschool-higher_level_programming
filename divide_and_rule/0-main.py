from h_fibonacci import FibonacciThread

fibo_threads = []
for i in range(20, 30):
    fibo_thread = FibonacciThread(i)
    fibo_threads += [fibo_thread]
    fibo_thread.start()

for t in fibo_threads:
    t.join()
