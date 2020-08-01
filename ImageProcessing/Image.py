from PIL import Image

img = Image.open("./Resource/squirtle.jpg")
size = (400, 400)
img.thumbnail(size)
img.show()
print(img.size)
