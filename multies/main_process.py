import multiprocessing
import time

t1 = time.perf_counter()

def do_something(sec=1):
    print(f'Start {sec}s')
    time.sleep(sec)
    print(f'ends {sec}s')
    return sec

threads = []

for _ in range(100):
    thread = multiprocessing.Process(target=do_something)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

t2 = time.perf_counter()

dt = t2 - t1

print(f'Finished {dt} second')