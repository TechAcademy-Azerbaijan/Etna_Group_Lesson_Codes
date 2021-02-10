# import time

def gen(max_value):
    i = 0
    while True:
        if i < max_value:
            yield i
            i += 1
        else:
            break
        

# g =  

for i in gen(10000):
    print(i)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# t1 = time.perf_counter()

# a = (x for x in range(100000000))

# print(a)
# t2 = time.perf_counter()

# dt = t2-t1
# print(dt)
# print(next(a))
# print(next(a))
# print(next(a))
# print(a[1])
# print(a[2])