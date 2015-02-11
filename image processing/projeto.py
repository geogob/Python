# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 02:59:31 2015
@authors: George Barros && Diego Leite

Universidade Estadual de Feira de Santana - UEFS.
Fundação Osvaldo Cruz - Fiocruz.
PathoSpot: Research Project - Computer Vision System from identification of kidney lesions by histological images.
Feira de Santana/BA, Brasil.
--------------------------------------------------------------------------------------------
OBS:

As etapas do nosso sistema de visão computacional são, de modo geral:

    1 - Pré-Processamento{ Ajuste de intensidade de pixels, eliminação de ruídos, etc}
    2 - Seguimentação{ Identificação dos núcleos, e atribuição de um valor padrão, com o qual nós possamos identifica-los}
    3 - Extração de Características{ Extrair os clusters, contar os núcleos por cluster}
    4 - Interpretação ou Classificação{ Processo de Classificação, utilização do classificador, se for necessário. Ou o IF}

"""
from pylab import *
import ia636 as ia #Utilizei nas operações matemáticas com a imagem, na etapa de pré-processamento
from ia636 import iacircle
from skimage.filter import threshold_otsu # Binarização
from skimage.restoration import denoise_tv_chambolle # Filtro de Suavização
from skimage  import img_as_ubyte 
#from skimage.color import rgb2gray
from skimage import io
from skimage.feature import blob_log, blob_dog, blob_doh
from PIL import Image, ImageOps
from matplotlib import pyplot
from math import sqrt

imRGB = Image.open('img/norma3.jpg') #imagem RGB
imGrayLevel = array(imRGB.convert('L'))# Convertendo imagem para nível de cinza
#imRGB = array(imRGB) #Mudando o tipo da imagem pra poder realizar as operações
#FIGURA 1
fig, ax = plt.subplots(2, 3, figsize=(14, 8))
fig.suptitle('PathoSpot - Pre-processing and threshold')
ax1, ax2, ax3, ax4, ax5, ax6= ax.ravel()


"""............PRÉ-PROCESSAMENTO..........."""
def preProcessing(imGrayLevel):
    
    #Escopo de algumas Operações básicas utilizadas no pré-processamento:
    #..............................................
    h = ia.iahistogram(imGrayLevel) #Equalização...
    n = imGrayLevel.size
    T = 255./n * np.cumsum(h)
    T = T.astype(uint8)
    #..............................................
    T1 = np.arange(256)  # função identidade
    T2 = ia.ianormalize(np.log(T1+30)) # logaritmica - realce partes escuras
    
    
    #T5 = ia.ianormalize(T1/50) # reduz o número de níveis de cinza
    #..................................................
    
    ax1.imshow(imRGB)
    ax1.set_title('rgb')
    
    ax2.imshow(imGrayLevel, vmin=0, vmax=255, cmap=plt.cm.gray)
    ax2.set_title('gray level')
    
    imGrayLevel =  denoise_tv_chambolle(imGrayLevel, weight=0.1, multichannel=True)
    imGrayLevel = img_as_ubyte(imGrayLevel)#Conversão de Float para UINT-8
    ax3.imshow(imGrayLevel, vmin=0, vmax=255, cmap=plt.cm.gray) #Filtro de suavização de textura
    ax3.set_title('tv signal filter')
    
    realceNucleos = T2[T[imGrayLevel]] #Realce de partes escuras da imagem equalizada
    ax4.imshow(realceNucleos, vmin=0, vmax=255, cmap=plt.cm.gray) 
    ax4.set_title('logaritimica')
    return realceNucleos
    
"""...........SEGUIMENTAÇÃO..........."""
def seguimentacao(realceNucleos):
    T1 = np.arange(256)  # função identidade
    T3 = 255 - T1 # negativo
    
    """ TESTAR A OTSU ADAPTIVO - LOCAL // DEPOIS"""
    #Binarização - Otsu Global
    global_thresh = threshold_otsu(realceNucleos)
    global_thresh = global_thresh - 42
    binary_global = realceNucleos > global_thresh
    binary_global = img_as_ubyte(binary_global) #Conversão de Float para UINT-8
    ax5.imshow(binary_global, vmin=0, vmax=255, cmap=plt.cm.gray)
    ax5.set_title('global otsu')
 
   #Aplicando função matemática de inversão - Só utilizo aqui para ilustrar o processo. A mesma operação é realizada antes da aplicação do Blob detection
    imSeguim = T3[binary_global]
    
    ax6.imshow(imSeguim, vmin=0, vmax=255, cmap=plt.cm.gray) 
    ax6.set_title('negative')
    im = Image.fromarray(uint8(binary_global)) #transformando a imagem em um array do tipo PIL OBJECT - Isso facilitará ao aplicar as próximas funções.
    im.save("x.jpg") #Salvando a imagem antes binário sem inversão
    

""".....EXTRAÇÃO DE CARACTERÍSTICAS....."""
def blobDetection(min_s, max_s, sigma):
    # Run Blob Detection by Laplacian of Gaussian (LoG)
    blobs_log = blob_log(image, max_s, threshold=.01)
    
    # Compute radii in the 3rd column
    blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
    
    # Configure the graph
    fig, ax = pyplot.subplots(1, 1)
    fig.suptitle('PathoSpot - Feature Extraction - Blob detection')     
    ax.set_title("Laplacian of Gaussian, min_s=" + str(min_s) + ", max_s="
			 + str(max_s) + ", sigma=" + str(sigma))
    ax.imshow(image, vmin=0, vmax=255, cmap=pyplot.cm.gray)   
    
    # Load graph
    for blob in blobs_log:
        y, x, r = blob
        c = pyplot.Circle((x, y), r, color='yellow', linewidth=2, fill=False)
        ax.add_patch(c)
    
    return blobs_log;
        
def cropBlobs(image, blobs):
    #......................................
    T1 = np.arange(256)  # função identidade
    T4 = 255 * (T1 > 128) # threshold 128
    image = T4[image]
    #.....................................
    h,w = image.shape #dimensões da imagem
    tam, tuplas = blobs.shape #dimensões da lista de bolhas
    listaCropBlobs = [None]*tam; #Lista Vazia do tamanho da quantidade de blobs (bolhas)
    i=0
    for blob in blobs:
        y, x, r = blob
        #Atribuindo coordenadas que serão utilizadas no fatiamento
        wi = x-r
        wf = x+r
        hi = y-r
        hf = y+r
        #Verificando os limites da imagem
        if wi<0:
            wi=0
        if wf>(w-1):
            wf=w-1 
        if hi<0:
            hi=0
        if hf>(h-1):
            hf=h-1
            
        #Fatiamento
        region = image[hi:hf, wi:wf]
        listaCropBlobs[i] = region #Armazena em uma lista
        i+=1;
        
    return listaCropBlobs

    
def watershedSeguim(im):
    #Segmenta as subimagens obtidas com o algoritmo watershed, o mesmo separa os objetos que estão unidos.
    print "Seguimentação das Submatrizes HERE !"
    
def blobDetectionSubIm(im):
    #Aplicamos novamente o blob detection nas submatrizes e enfim, contamos os núcleos.
    print "Segunda Aplicação do Blob detection com parâmetros ajustados para essa nova tarefa, identificar os núcleos individualmente."

"""...CLASSIFICAÇÃO....."""
def classificacao():
    #Classificaos as imagens por meio um classificador, provavelmente linear (IF)
    print "Classificacao da imagem: Normal ou Anormal"
    
#Pré-Processamento
realceNucleos = preProcessing(imGrayLevel)

#Seguimentação
imSeguim = seguimentacao(realceNucleos) 
image = Image.open("x.jpg" ) #Caminho padrão da imagem salva na última etapa
image = ImageOps.invert(image)#Inversão da imagem 
image.save("inverted.jpg")
image = io.imread("inverted.jpg", as_grey=False)
imageCopy = image


#Extração de características
blobs = blobDetection(1, 10, 30)
listaCropBlobs = cropBlobs(imageCopy, blobs)
fig3, ax = pyplot.subplots(1, 1)
fig.suptitle('Fatiamento - Ex: SubImagem 35')
ax.imshow(listaCropBlobs[35])
    
#..................................................................
plt.show() #Mostrar tudo