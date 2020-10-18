from PIL import Image

img = Image.open('baby.jpeg')

# img.show()

# print(img.mode)

r, g, b = img.split()

r.show()
g.show()
b.show()
