# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 14:29:03 2014

@author: George Oliveira Barros. 
Aprendendo interface gráfica em Python.
"""

from Tkinter import *
class Janela:
    def __init__(self,toplevel):
        #frames
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        
        self.fr2 = Frame(toplevel)
        self.fr2.pack()
        
        #Bottons
        self.botao = Button(self.fr2, text='button 1')
        self.botao['bg']='white'
        self.botao['font']=('Arial','12')
        self.botao['height']=10
        self.botao['width']=10
        self.botao.pack(side=LEFT)
        
        self.botao2 = Button(self.fr2, text='button 2')
        self.botao2['bg']='gray'
        self.botao2['font']=('Arial','12')
        self.botao2['height']=5
        self.botao2['width']=10
        self.botao2.pack()
        
        
raiz=Tk()
Janela(raiz)
raiz.mainloop()
