# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 21:04:46 2014

@author: gob

Trabalho prático 01 - Fundamentos de Processamento de Imagens - PGCA Mestrado - UEFS, BA.

My Home, my life

"""

from Tkinter import *

#testando o armazenamento em variáveis
a=(220,418)

class Kanvas:
        def __init__(self,raiz):
            self.canvas = Canvas(raiz, width=580, height=420,  bd=5, bg='white')
            
            #Retangulo:
            #De a para b
            self.canvas.create_line(a, (360,418))
            #De b para c
            self.canvas.create_line((360,418), (360,280))
            #De c para d
            self.canvas.create_line((360,280), (220,280))
            #De d para a
            self.canvas.create_line((220,280), (220,418))
            
            #De e para as extremidades superiores do retangulo
            self.canvas.create_line((290,190), (360,280))
            self.canvas.create_line((290,190), (220,280))
            
            #triangulo:
            
            
            
                        
                        
            
            
            self.canvas.pack()            

instancia=Tk()
Kanvas(instancia)
instancia.mainloop()