# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 15:13:13 2014

@author: gob
"""

from PIL import Image
from pylab import *
import ia636 as ia

im = array(Image.open('img/rosa.jpg').convert('L')) # read image to array
#Imagem 
figure()# create a new figure
gray() # don't use colors
imshow(im)

#Histograma da Imagem
figure()
hist(im.flatten(),128)

#equalização
h = ia.iahistogram(im)
n = im.size
T = 255./n * np.cumsum(h)
T = T.astype(uint8)
g = T[im]

#Imagem equalizada
figure()
'''l,c = g.shape;
for i in xrange(l):
    for j in xrange(c):
        if g[i,j]>200:
            g[i,j] = 0;
        else:
            g[i,j] = 0;'''
        
            
    
imshow(g)

#Histograma da Imagem equalizada
figure()
hist(g.flatten(),128)


#mostrar os componentes de exiibição
show()