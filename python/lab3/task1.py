from skimage import io
import argparse
from skimage.transform import rotate
import matplotlib.pyplot as plt
from skimage.util import random_noise
from skimage.filters import gaussian
from skimage.exposure import adjust_gamma
from skimage.color import rgb2gray
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument('data_path')
commands = input().split(' ')
for direc in ['cleaned', 'dirty']:
    i=20
    imgs = io.imread_collection(parser.parse_args().data_path+'/'+direc+'/*')
    for img in imgs:
        for com in commands:
            new_img=img
            if com == 'turn':
                new_img=(rotate(img,90)*255).astype(np.uint8)
            elif com == 'noise':
                new_img=(random_noise(img, var=0.1**.01)*255).astype(np.uint8)
            elif com == 'gauss':
                new_img=(gaussian(img, sigma=2)*255).astype(np.uint8)
            elif com == 'gamma':
                new_img=adjust_gamma(img,gamma=2)
            elif com == 'gray':
                new_img=(rgb2gray(img)*255).astype(np.uint8)
            elif com == 'complex':
                new_img= (rotate(random_noise(rgb2gray(img),var=0.1**.01),90)*255).astype(np.uint8)
            io.imsave(parser.parse_args().data_path+'/'+direc+f'/{i:>04}.jpg',new_img)
            i+=1