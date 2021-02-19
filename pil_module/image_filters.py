from PIL import Image, ImageFilter

bmw = Image.open('bmw.jpg')

new_bmw = bmw.filter(ImageFilter.GaussianBlur(10))
new_bmw.show()