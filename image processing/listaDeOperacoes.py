# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 15:13:13 2014

@author: George O. Barros
"""

from PIL import Image
from pylab import *
import ia636 as ia

imRGB = array(Image.open('img/teste/prob2.jpg')) #imagem RGB
imGrayLevel = array(Image.open('img/teste/prob2.jpg').convert('L'))# Imagem em nível de cinza

#.................................................FIGURA 1
fig, ax = plt.subplots(2, 4, figsize=(14, 8))
fig.suptitle('George O. Barros - some operations')
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8 = ax.ravel()

#Operações:
#..............................................
h = ia.iahistogram(imGrayLevel) #Equalização...
n = imGrayLevel.size
T = 255./n * np.cumsum(h)
T = T.astype(uint8)
#..............................................
T1 = np.arange(256)  # função identidade
T2 = ia.ianormalize(np.log(T1+1)) # logaritmica - realce partes escuras
T3 = 255 - T1 # negativo
T4 = 255 * (T1 > 128) # threshold 128
T5 = ia.ianormalize(T1/50) # reduz o número de níveis de cinza

g = np.copy(imRGB) #Quadriculado sobreposto
g[::10,:]=255
g[:,::10]=255

#PLOTS:
ax1.imshow(imRGB)
ax1.set_title('RGB')

ax2.imshow(imGrayLevel, vmin=0, vmax=255, cmap=plt.cm.gray)
ax2.set_title('Gray Level (0-255)')

ax3.imshow(T2[T[imGrayLevel]], vmin=0, vmax=255, cmap=plt.cm.gray) #Realce de partes escuras da equalização de uma imagem x: t2(t(x))
ax3.set_title('logaritmica - realce partes escuras')

#T[ia.ianormalize(T3[imGrayLevel]).astype(np.uint8)]

ax4.imshow(T3[imGrayLevel], vmin=0, vmax=255, cmap=plt.cm.gray)
ax4.set_title('Negative')

ax5.imshow(T4[imGrayLevel], vmin=0, vmax=255, cmap=plt.cm.gray)
ax5.set_title('threshold 128')

ax6.imshow(T5[imGrayLevel], vmin=0, vmax=255, cmap=plt.cm.gray)
ax6.set_title('gray level redution')

ax7.imshow(T[imGrayLevel], vmin=0, vmax=255, cmap=plt.cm.gray)
ax7.set_title('Equalization')

ax8.imshow(g, vmin=0, vmax=255, cmap=plt.cm.gray)
ax8.set_title('Sobreposto')

plt.show() #Mostrar tudo