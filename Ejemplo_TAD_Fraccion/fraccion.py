# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 07:59:15 2022

@author: jorda
"""

def mcd(a, b):
    '''
    Obtiene el máximo común divisor (MCD) entre dos números aplicando el algoritmo de Euclides.
    Parameters
    ----------
    a : Entero positivo.
    b : Entero positivo.
    Returns
    -------
    a : Entero positivo.
        Es el máximo común divisor calculado.
    '''
    while b:
        a, b = b, a % b
    return a


class Fraccion:
    def __init__(self,arriba,abajo):
        self.num = arriba
        self.den = abajo
        
    def __str__(self):
        cad = str(self.num)
        if self.den != 1:
            cad += "/"+str(self.den)    
        return cad
        
    def __add__(self,otraFraccion):
        nuevoNum = self.num*otraFraccion.den + self.den*otraFraccion.num
        nuevoDen = self.den * otraFraccion.den
        comun = mcd(nuevoNum,nuevoDen) #algoritmo de Euclides
        return Fraccion(nuevoNum//comun,nuevoDen//comun)
    
