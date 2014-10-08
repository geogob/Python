# -*- coding: utf-8 -*-
"""
Created on Tue Sep 09 20:41:33 2014

@author: George O. Barros
"""

#from PIL import Image
#from pylab import *
import numpy as np
import time

#pil_im = Image.open('cheio.jpg')
#pil_im_gray = pil_im.convert('F')
#imshow(pil_im)

colorido = adread('rosa.jpg')
print 'Dimensões:    ', colorido.shape
