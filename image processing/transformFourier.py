# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 00:32:27 2014

@author: gob
"""
from ia636 import *
from numpy import *

im = array(Image.open('img/confuso.jpg'))
#F = iadft(im)
#Fv = iadftview(F)
#F = np.fft.fft2(image)


imshow(im)

F = iadft(f)

