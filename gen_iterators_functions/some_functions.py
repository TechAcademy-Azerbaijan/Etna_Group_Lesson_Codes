
names = ['Ali', 'Yusif', 'Yusif', 'Qedir', 'Emrah', 'Sukran']
surnames = ['Abdiyev', 'Cebrayilov', 'Huseynli', 'Mirzeyev', 'Bagirov', 'Cabbarov']
ages = [1,2,3,4,5,6]

combine = zip(names, surnames, ages)

print(list(combine))
# from functools import reduce
# a = [4,2,46,878,2, 3, '4', 'a',]

# def sum_numbers(_sum, i):
#     if isinstance(i, int):
#         return _sum + i
#     return _sum

# sum_value = reduce(sum_numbers, a)

# sum_value = reduce(lambda _sum, i: _sum + i  if isinstance(i, int) else _sum , a)
# # ternary
# print(sum_value)




# for i in a:
#     s += i

# b = []

# def is_even(i):
#     return i % 2 == 0

# b = filter(lambda i: i%2 == 0, a)
# print(list(b))

# def square(i):
#     return i ** 2

# square_a = map(lambda i: i**2, a)
# print(list(square_a))


