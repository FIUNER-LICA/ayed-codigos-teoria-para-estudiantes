#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:12:26 2022

@author: jinsfran
"""

class MiClase:
    campo_de_clase_1 = 11
    campo_de_clase_2 = 22
    
    def __init__(self):
        self.campo_de_instancia_1 = 1
        self.campo_de_instancia_2 = 2
        
        self.campo_publico = 'público'
        self._campo_protegido = 'protegido'
        self.__campo_privado = 'privado'
    
    def __str__(self):
        cad = 'Campos:\n'
        cad += '\tDe instancia: '
        cad += str(self.campo_de_instancia_1) + ', '
        cad += str(self.campo_de_instancia_2) + '\n'
        cad += '\tDe clase: '
        cad += str(MiClase.campo_de_clase_1) + ', '
        cad += str(MiClase.campo_de_clase_2)
        return cad
    
    def metodo_de_instancia_1_sin_argumentos(self):
        pass
    
    def metodo_de_instancia_2_con_argumentos(self, arg_a, arg_b):
        pass
    
    def metodo_de_clase_sin_argumentos():
        pass
    
    def metodo_de_clase_con_argumentos(arg_1, arg_2):
        pass
    
    
# "instancia" es equivalente a "objeto"
# Una instancia "se crea" a partir de una clase
# A partir de una clase se pueden crear múltiples instancias

instancia_1 = MiClase()   # SE CREA una instancia
instancia_2 = MiClase()   # SE CREA una instancia

print(instancia_1)
print(instancia_2)

instancia_1.campo_de_instancia_1 = 100
instancia_2.campo_de_instancia_2 = 200

print()
print('instancia_1: ', instancia_1)
print('instancia_2: ', instancia_2)

# instancia_1.campo_de_clase_1 = 1111  
   # OJO! Acabamos de crear un nuevo campo! No queremos eso...

MiClase.campo_de_clase_1 = 1111

print()
print('instancia_1: ', instancia_1)
print('instancia_2: ', instancia_2)

print()
print()