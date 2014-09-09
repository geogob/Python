# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 21:04:46 2014

@author: George O. Barros

Trabalho prático 01 - Fundamentos de Processamento de Imagens - PGCA Mestrado - UEFS, BA.

My Home, my life

"""
from math import *
from Tkinter import *
import numpy as np

#Entrada de informações para transformações geométricas:
dx = int(raw_input ('Informações para Translação -- Informe o dx:'))
dy = int(raw_input ('Informações para Translação -- Informe o dy:'))
dy = dy*(-1)
fatorEscala = float(raw_input ('Fator de escala:'))
rotacao = int(raw_input ('Rotação (em graus):'))


#Coordenadas iniciais --> levando em consideração a representação matricial do Python
a=[220,418]
b=[360,418]
c=[360,280]
d=[220,280]
e=[290,190]

#Classe canvas (É o componente gráfica para representar formas geométricas e animações)
class Kanvas:
    
    
        def __init__(self,raiz):
            
            #propriedades da tela de exibição
            self.canvas = Canvas(raiz, width=800, height=600,  bd=2, bg='white')
            
            #Formando a casinha com retas entre os pares ordenados (vetores)
            self.canvas.create_line(a, b) #De a para b
            self.canvas.create_line(b, c) #De b para c
            self.canvas.create_line(c, d) #De c para d
            self.canvas.create_line(d, a) #De d para a
            self.canvas.create_line(e, c) #De e para as extremidades superiores{e-c, && e-d}
            self.canvas.create_line(e, d)
            
            
            a[0] = a[0] + dx
            a[1] = a[1] + dy
            
            b[0] = b[0] + dx
            b[1] = b[1] + dy
            
            c[0] = c[0] + dx
            c[1] = c[1] + dy
            
            d[0] = d[0] + dx
            d[1] = d[1] + dy
            
            e[0] = e[0] + dx
            e[1] = e[1] + dy
                     
            
            #exibindo            
            self.canvas.create_line(a, b) #De a para b
            self.canvas.create_line(b, c) #De b para c
            self.canvas.create_line(c, d) #De c para d
            self.canvas.create_line(d, a) #De d para a
            self.canvas.create_line(e, c) #De e para as extremidades superiores{e-c, && e-d}
            self.canvas.create_line(e, d)


            #FATOR DE ESCALA
            a[0] = a[0] * fatorEscala
            a[1] = a[1] * fatorEscala
            
            b[0] = b[0] * fatorEscala
            b[1] = b[1] * fatorEscala
            
            c[0] = c[0] * fatorEscala
            c[1] = c[1] * fatorEscala
            
            d[0] = d[0] * fatorEscala
            d[1] = d[1] * fatorEscala
            
            e[0] = e[0] * fatorEscala
            e[1] = e[1] * fatorEscala
            
            #exibindo                        
            self.canvas.create_line(a, b) #De a para b
            self.canvas.create_line(b, c) #De b para c
            self.canvas.create_line(c, d) #De c para d
            self.canvas.create_line(d, a) #De d para a
            self.canvas.create_line(e, c) #De e para as extremidades superiores{e-c, && e-d}
            self.canvas.create_line(e, d)
            

            
            #ROTAÇÃO            

            seno = sin(radians(rotacao))
            cosseno = cos(radians(rotacao))
            
            
            a[0] = int((cosseno * a[0]) - (seno * a[1]) )#novo x
            a[1] = int((seno * a[0]) + (cosseno * a[1]) )#novo y
            
            b[0] = int((cosseno * b[0]) - (seno * b[1]) )#novo x
            b[1] = int((seno * b[0]) + (cosseno * b[1]) )#novo y 
            
            c[0] = int((cosseno * c[0]) - (seno * c[1]) )#novo x
            c[1] = int((seno * c[0]) + (cosseno * c[1]) )#novo y
            
            d[0] = int((cosseno * d[0]) - (seno * d[1]) )#novo x
            d[1] = int((seno * d[0]) + (cosseno * d[1]) )#novo y            
            
            e[0] = int((cosseno * e[0]) - (seno * e[1]) )#novo x
            e[1] = int((seno * e[0]) + (cosseno * e[1]) )#novo y  

            #exibindo            
            self.canvas.create_line(a, b) #De a para b
            self.canvas.create_line(b, c) #De b para c
            self.canvas.create_line(c, d) #De c para d
            self.canvas.create_line(d, a) #De d para a
            self.canvas.create_line(e, c) #De e para as extremidades superiores{e-c, && e-d}
            self.canvas.create_line(e, d)
            
            self.canvas.pack()  
               
instancia=Tk()
Kanvas(instancia)
instancia.mainloop()



            ##Comentários registrando outra forma de processar as transformações(Através de operações matriciais)
            #Transformações geométricas // Manualmente
            
            #TRANSLAÇÃO
            #matrizDeTranslacao = np.array([[1,0,dx],[0,1,dy],[0,0,1]])
            
            #Atribuindo o elemento neutro 1 no vetor de coordenadas (Outra forma de fazer)
            #tranA = a + [1]
            #tranB = b + [1]
            #tranC = c + [1]
            #tranD = d + [1]
            #tranE = e + [1]
            
            #multiplica a matriz de translação e o vetor de coordenadas            
            #newA = np.dot(matrizDeTranslacao,tranA)
            #newB = np.dot(matrizDeTranslacao,tranB)
            #newC = np.dot(matrizDeTranslacao,tranC)
            #newD = np.dot(matrizDeTranslacao,tranD)
            #newE = np.dot(matrizDeTranslacao,tranE)
            #Impressão das coordenadas modificadas