# from PIL import Image, ImageFilter

# bmw = Image.open('bmw.jpg')

# new_bmw = bmw.filter(ImageFilter.GaussianBlur(10))
# new_bmw.show()


def make_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


counter = make_counter()

print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
