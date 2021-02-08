

class Human:
    __age = 0

    def __init__(self, name, surname):
        self.first_name = name
        self.last_name = surname

    def eat(self):
        print('Yemek yedim')

    def sleep(self):
        print('Dinceldim')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise Exception('Insanin yasi duzgun verilmeyib')
        if new_age < self.__age:
            raise Exception('Insanin yasi azala bilmez')
        self.__age = new_age


class Programmer:
    def eat(self):
        print('Gece 12-de yemek yedim')

class Employee(Programmer, Human):
    # department = 'IT'

    # overiding
    def __init__(self, name, surname, department):
        super(Programmer, self).__init__(name, surname)
        self.department= department

    def work(self):
        print('I am worked')
    


# print(Human.age)
# print(Human.first_name)

yusif_obj = Employee('Yusif', 'Huseynli', 'Sales')
emrah_obj = Employee('Emrah', 'Bagirov', 'IT')
yusif_obj.eat()

print(f'Menim adim {yusif_obj.first_name}, Soyadim {yusif_obj.last_name }dir, \
    departamentim {yusif_obj.department}')
print(f'Menim adim {emrah_obj.first_name}, Soyadim {emrah_obj.last_name }dur \
departamentim {emrah_obj.department}')

print(isinstance(yusif_obj, Human))


# yusif_obj.__age += 1

print(f'yasim  { yusif_obj.age }')
yusif_obj.age += 1
yusif_obj.age += 1
yusif_obj.age += 1
print(f'yasim  { yusif_obj.age }')
# print('Yasim', yusif_obj.__age)