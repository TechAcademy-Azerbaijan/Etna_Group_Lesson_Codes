import time
# import threading
import concurrent.futures


t1 = time.perf_counter()

def do_something(sec):
    print(f'Start {sec}s')
    time.sleep(sec)
    return sec

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    e = [executor.submit(do_something, sec) for sec in secs]
    s = 0
    for future in concurrent.futures.as_completed(e):
        s += int(future.result())
        
print(s)

t2 = time.perf_counter()

dt = t2 - t1

print(f'Finished {dt} second')