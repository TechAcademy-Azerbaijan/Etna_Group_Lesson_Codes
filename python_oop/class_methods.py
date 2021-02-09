from datetime import datetime

# dt = datetime(8, 2, 2021, 12,0)

# dt = datetime.strftime('08/02/2021/12/00/00', '%d/%m/%Y') #  datetime(8, 2, 2021, 12,0)

class Employee:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def format_str(cls, name_str): # "Ali Abdiyev 17"
        name, surname, age = name_str.split() #['Ali', 'Abdiyev', 17]
        return cls(name, surname, age)

    @staticmethod
    def work():
        print('Employee always worked')

    @classmethod
    def set_age(cls, new_age):
        cls.age = new_age

# employee_data = input('Adinizi Soyadinizi ve yasinizi daxil edin: (Format: Name Surname age) ')

Employee.work()

# ali = Employee.format_str(employee_data)

# print(ali.name)

# User.query.all()

# ali = Employee('Ali', 'Abdiyev')

# Employee.set_age(18)
# yusif = Employee('Yusif', 'Huseynli')
# print(ali.age)

# # yusif.age = 20
# print(yusif.age)



