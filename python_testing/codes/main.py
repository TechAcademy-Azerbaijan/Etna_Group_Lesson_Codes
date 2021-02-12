

def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("You can't divide by zero")
    return x / y
