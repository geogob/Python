# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 21:15:55 2014

@author: George Oliveira Barros
"""

from PIL import Image
from pylab import *
import ia636 as ia
from skimage.filter import threshold_otsu
from skimage.restoration import denoise_tv_chambolle
from  skimage  import img_as_ubyte


imRGB = Image.open('img/teste/prob3.jpg') #imagem RGB
imGrayLevel = array(imRGB.convert('L'))# Convertendo imagem para nível de cinza
imRGB = array(imRGB)
#.................................................FIGURA 1
fig, ax = plt.subplots(2, 3, figsize=(16, 12))
fig.suptitle('PathoSpot - Pre-processing and threshold')
ax1, ax2, ax3, ax4, ax5, ax6= ax.ravel()

#Escopo de Operações:
#..............................................
h = ia.iahistogram(imGrayLevel) #Equalização...
n = imGrayLevel.size
T = 255./n * np.cumsum(h)
T = T.astype(uint8)
#..............................................
T1 = np.arange(256)  # função identidade
T2 = ia.ianormalize(np.log(T1+4)) # logaritmica - realce partes escuras
T3 = 255 - T1 # negativo
T4 = 255 * (T1 > 128) # threshold 128
T5 = ia.ianormalize(T1/50) # reduz o número de níveis de cinza
#..................................................
    
#PLOTS:
#.........................................................Pre-Processamento e Seguimentação
ax1.imshow(imRGB)
ax1.set_title('rgb')

ax2.imshow(imGrayLevel, vmin=0, vmax=255, cmap=plt.cm.gray)
ax2.set_title('nivel de cinza')

imGrayLevel =  denoise_tv_chambolle(imGrayLevel, weight=0.1, multichannel=True)
imGrayLevel = img_as_ubyte(imGrayLevel)#Conversão de Float para UINT-8

ax3.imshow(imGrayLevel, vmin=0, vmax=255, cmap=plt.cm.gray) #Filtro de suavização de textura
ax3.set_title('tv signal filters')



realceNucleos = T2[T[imGrayLevel]] #Realce de partes escuras da imagem equalizada
ax4.imshow(realceNucleos, vmin=0, vmax=255, cmap=plt.cm.gray) 
ax4.set_title('realce dos nucleos') # Função Logarítimica Adessowiki - Realce de partes escuras

#Binarização - Otsu Global
global_thresh = threshold_otsu(realceNucleos)
global_thresh = global_thresh - 22
binary_global = realceNucleos > global_thresh
binary_global = img_as_ubyte(binary_global) #Conversão de Float para UINT-8

ax5.imshow(binary_global, vmin=0, vmax=255, cmap=plt.cm.gray)
ax5.set_title('Otsu Global')

ax6.imshow(T3[binary_global], vmin=0, vmax=255, cmap=plt.cm.gray) 
ax6.set_title('Inversao')

#.......................................Identificação de Lesões:

#Função de fatiamento e identificação de lesões HERE !!!

#..................................................................
plt.show() #Mostrar tudo