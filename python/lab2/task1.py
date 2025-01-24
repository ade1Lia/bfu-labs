from PIL import Image
image_path = 'test.jpg'
image = Image.open(image_path)
r,g,b = image.split()
image.show()
r.show()
g.show()
b.show()