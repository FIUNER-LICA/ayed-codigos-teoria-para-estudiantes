# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:06:37 2022

@author: jorda
"""

class Bolsa:
    def __init__(self):
        self.elementos = []

    def agregar(self, x):
        self.elementos.append(x)
        
    def agregar_doble(self, x):
        self.agregar(x)
        self.agregar(x)
        
    def __str__(self):
        self.str_contenido = ''

        for value in self.elementos:
            self.str_contenido +=  ' ' + str(value)
    
        return self.str_contenido

    def __del__(self):
        pass    # para literalmente "no hacer nada"
        # print('Se destruye la bolsa')
        
