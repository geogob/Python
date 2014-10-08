# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 15:13:13 2014

@author: gob
"""

from PIL import Image
from pylab import *
import ia636 as ia

im = array(Image.open('img/2.jpg').convert('L')) # read image to array

figure()# create a new figure
gray() # don't use colors
imshow(im)

figure()
hist(im.flatten(),128)

h = ia.iahistogram(im)
n = im.size
T = 255./n * np.cumsum(h)
T = T.astype(uint8)
g = T[im]
figure()
imshow(g)
figure()
hist(g.flatten(),128)


show()