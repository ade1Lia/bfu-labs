from PIL import Image
from skimage import io
import matplotlib.pyplot as plt
import argparse
import numpy as np
plt.figure(1, figsize=(8, 8))
parser = argparse.ArgumentParser()
parser.add_argument('img_path')
img = Image.open(parser.parse_args().img_path)
aximg = plt.axes()
aximg.imshow(img)
hist = plt.axes([0.9, 0.7, 0.2, 0.1])
hist.hist(img.histogram(), bins=1331)
img = io.imread(parser.parse_args().img_path)
r, g, b= img[:,:,0], img[:,:,1], img[:,:,2]
hist = plt.axes([0.9, 0.5, 0.2, 0.1])
hist.hist(r.flatten(), bins=1331)
hist = plt.axes([0.9, 0.3, 0.2, 0.1])
hist.hist(g.flatten(), bins=1331)
hist = plt.axes([0.9, 0.1, 0.2, 0.1])
hist.hist(b.flatten(), bins=1331)
plt.show()