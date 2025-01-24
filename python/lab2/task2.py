from PIL import Image
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('image_path')
image = Image.open(parser.parse_args().image_path)
r,g,b = image.split()
k1, k2, k3 = 0, 0, 0
for i in range(image.size[0]):
    for j in range(image.size[1]):
        k1 += r.getpixel((i,j))
        k2 += g.getpixel((i, j))
        k3 += b.getpixel((i, j))
if k1 == max(k1,k2,k3):
    print('r')
elif k2 == max(k1,k2,k3):
    print('g')
else:
    print('b')