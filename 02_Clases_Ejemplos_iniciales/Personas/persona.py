#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:15:09 2022

@author: jinsfran
"""

class Persona:
    contador = 0
    
    def __init__(self, p_nombre, p_apellido):
        self.nombre = p_nombre
        self.apellido = p_apellido
        Persona.contador += 1
        
    def __str__(self):
        cad = self.nombre + ' ' + self.apellido
        return cad
    
    def __del__(self):
        Persona.contador -= 1
        
