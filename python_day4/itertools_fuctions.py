import itertools as it
import operator

mylist = [5,3,2, 0, 8,1,9,4]



print(list(it.accumulate(mylist, operator.mul)))


# persons = [
#     {
#         'name': 'Tural',
#         'city': 'Baku',
#     },
#     {
#         'name': 'Ali',
#         'city': 'Istanbul',
#     },{
#         'name': 'Yusif',
#         'city': 'Gence',
#     },{
#         'name': 'Emrah',
#         'city': 'Baku',
#     },{
#         'name': 'Qedir',
#         'city': 'Gence',
#     },
#     {
#         'name': 'Sukran',
#         'city': 'Baku',
#     },
#     {
#         'name': 'Idris',
#         'city': 'Gence',
#     },
# ]

# def group_by_city(person):
#     return person['city']

# an_iterator = itertools.groupby(persons, group_by_city) 
  
# for key, group in an_iterator:
#     key_and_group = {key : list(group)} 
#     print(key_and_group)


# my_list = ['A', 'B', 'C', 'D']

# all_comb = itertools.product(my_list, repeat=4)

# for i in all_comb:
#     print(i)

# permutations = itertools.permutations(my_list, 2)

# for i in permutations:
#     print(i)

# combination = itertools.combinations(my_list, 2)

# for i in combination:
#     print(i)



# repeat = itertools.repeat(5)

# # def pow_five(x):
# #     return x ** 5

# print(list(map(pow, my_list, repeat)))


# print(next(repeat))
# print(next(repeat))
# print(next(repeat))

# counter = itertools.count(start=1, step=3)

# my_list = [4,5,6,7,8]

# print(list(zip(counter, my_list)))

# counter = itertools.cycle(['On', 'Off'])

# my_list = [4,5,6,7,8]

# print(list(zip(counter, my_list)))

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))