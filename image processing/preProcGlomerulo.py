# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 15:13:13 2014

Etapa de Pré-Processamento da imagem do glomérulo

Diego -> README = :) -> Você pode transformar esse arquivo em uma função: "preProcessamento". O retorno é a variável "image". 
                        O importante agora é usar essa variável no Blobdetection. Logo no final do código eu falo com mais detalhes. 
                        Vou criar uma programa que apenas chama as funções de PreProcessamento, 
                        depois Blob detection e conta os núcleos, por fim uma última de classificação.

@author: George O. Barros
    
"""
from skimage import io
from skimage.filter import threshold_otsu, rank
from PIL import Image
from pylab import *
import ia636 as ia
import numpy as np

imRGB = Image.open('img/z.jpg') #imagem RGB
imGrayLevel = np.array(imRGB.convert('L'))# Conversão para nível de cinza

#.................................................FIGURA
fig, ax = plt.subplots(2, 3, figsize=(20, 8))
fig.suptitle('PathoSpother - Pre-Processamento')
ax1, ax2, ax3, ax4, ax5, ax6 = ax.ravel()

#Operações:
#..............................................
h = ia.iahistogram(imGrayLevel) #Equalização...
n = imGrayLevel.size
T = 255./n * np.cumsum(h)
T = T.astype(uint8)
#..............................................

T1 = np.arange(256)  # função identidade
T3 = 255 - T1 # negativo
T4 = 255 * (T1 > 80) # threshold

#PLOTS:
ax1.imshow(imRGB) #mostro a imagem em RGB
ax1.set_title('rgb')

ax2.imshow(imGrayLevel, vmin=0, vmax=255, cmap=plt.cm.gray) #mostro a imagem em nível de cinza
ax2.set_title('gray level')

negativo = T3[imGrayLevel]
ax3.imshow(negativo, vmin=0, vmax=255, cmap=plt.cm.gray) #Calculo do negativo da imagem (inversão dos valores)
ax3.set_title('negative')

negativoEqual = T[negativo]
ax4.imshow(negativoEqual, vmin=0, vmax=255, cmap=plt.cm.gray) #Equalizo sem normalizar -> Agora funcionou, vai entender !!! :)
ax4.set_title('equalization')

#negativeEqualizNormaliz = T[ia.ianormalize(T3[imGrayLevel]).astype(np.uint8)]
ax5.imshow(negativoEqual, vmin=0, vmax=255, cmap=plt.cm.gray) #Normalizo (pra evitar overflow ou underflow) e depois equalizo
ax5.set_title('normaliz. e equaliz.')

image = T4[negativoEqual] #Essa variável: "image" é o parâmetro de entrada do algoritmo Blob detection

ax6.imshow(image, vmin=0, vmax=255, cmap=plt.cm.gray) #limiarização - binarizo a imagem, como 0 ou 255. Utilizo com valor limiar = 100
ax6.set_title('threshold') 
#Threshold
#http://scikit-image.org/docs/dev/auto_examples/plot_local_otsu.html

io.imsave('pb.jpg', image)

plt.show() #Mostrar tudo

''' Observação: 
    
    O processo de limiarização ainda necessita ser melhorado, 
    estou utilizando um limiar fixo igual a 100, quando na verdade deveria utilizar 
    um algoritmo de limiarização automática (Otsu por exemplo). Esse algoritmo detectará o melhor valor de limiar para cada imagem.
    No entanto, nosso objetivo atual é apenas testar o desempenho do Blob detection, então por enquanto, serve !
    Vlw! Abraço! Espero que dê tudo certo! '''
