import time
import datetime
# import threading
import concurrent.futures
import requests


t1 = time.perf_counter()

def download_image(url):
    r = requests.get(url)

    with open(f'images/{datetime.datetime.now()}.jpg', 'wb') as f:
        f.write(r.content)

with concurrent.futures.ProcessPoolExecutor() as executor:
    url = 'https://picsum.photos/500/500'
    for _ in range(100):
        executor.submit(download_image, url)


t2 = time.perf_counter()

dt = t2 - t1

print(f'Finished {dt} second')