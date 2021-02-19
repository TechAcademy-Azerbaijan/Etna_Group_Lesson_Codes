import os
from PIL import Image

image = Image.open('bmw.jpg')

size = (300, 300)

# print(image.size, image.mode)

# new_image = image.resize(size)
# new_image.show()
# print(new_image.size, new_image.mode)



for file in os.listdir('.'):
    file_name, file_ext = os.path.splitext(file)
    if file_ext == '.jpg':
        image = Image.open(file)
        new_image = image.resize(size)
        rotated_image = image.rotate(90)
        rotated_image.save(f'rotated/{file}')
        new_image.save(f'300/{file}')
        image.thumbnail(size)
        image.save(f'thumb_300/{file}')
