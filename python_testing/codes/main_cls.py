
class Calc:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def divide(self):
        if self.y == 0:
            raise ZeroDivisionError("You can't divide by zero")
        return self.x / self.y
