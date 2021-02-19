from PIL import Image, ImageDraw
bmw = Image.open('bmw.jpg')
bugatti = Image.open('hyundai.jpg').resize(bmw.size)

mask = Image.new( 'L', bmw.size, 255)
x, y =  bugatti.size

draw = ImageDraw.Draw(mask)

draw.ellipse((x/2-150, y/2-150, x/2+150, y/2 + 150), fill=0)

new_image = Image.composite(bmw, bugatti, mask)
new_image.show()
# print(mask.size)