# a = [4,2,6,3,9]

# class PowTwo:

#     def __init__(self, max_value):
#         self.max = max_value

#     def __iter__(self):
#         self.i = 0
#         return self
    
#     def __next__(self):
#         if self.i < self.max:
#             result = self.i ** 2
#             self.i += 1
#             return result
#         else:
#             raise StopIteration

# i_pow_two = iter(PowTwo(6))

# while True:
#     try:
#         print(next(i_pow_two))
#     except StopIteration:
#         break

# print(iter(PowTwo(6)))

# for i in PowTwo(6):
#     print(i)

# i = a.__iter__()

# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break


# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for i in a:
#     print(i)