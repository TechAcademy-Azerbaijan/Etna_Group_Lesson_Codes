

# class Library:

#     def __init__(self):
#         self.books = ['Incognito']
#         self.authors = []

#     def __repr__(self):
#         if not self.books:
#             return 'Hec bir kitab yoxdur'
#         book_str = 'Kitablar: \n'
#         for book in self.books:
#             book_str += book + '\n'
#         return book_str

#     def __add__(self, new_book):
#         self.books.append(new_book)

#     def __sub__(self, rm_book):
#         self.books.remove(rm_book)

# l = Library()
# print(l)
# new_book = input('Elave etmek istediyiniz kitabi daxil edin: ')
# l + new_book
# print('Elave edildi')
# print(l)
# rm_book = input('Silmek istediyiniz kitabi daxil edin: ')
# l - rm_book
# print("Kitab silindi")
# print(l)


class Int:

    def __init__(self, value):
        self.value = value

    def __add__(self, value):
        return self.value + value + 1

    def __str__(self):
        return f'{self.value}'

a = Int(5)
a += 6
print(a)

# b = 10
# b += 10
# print(b)

