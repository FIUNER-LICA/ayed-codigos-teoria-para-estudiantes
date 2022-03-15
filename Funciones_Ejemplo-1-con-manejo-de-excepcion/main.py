#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:44:18 2022

@author: jinsfran
"""

# --------------------------------------------
# Una definición de función con dos argumentos
# --------------------------------------------
def mayor(valor1, valor2):
    mas_grande = valor1
    if valor2 > valor1:
        mas_grande = valor2	
    return mas_grande


# Salidas por consola del resultado de aplicar la función a pares de datos de diferente "tipo"
print('1:', mayor("ABC", "ABG"))          # string
print('2:', mayor('ABC', 'ABG'))
print('3:', mayor(4, 7))                  # int
print('4:', mayor(1.5, 0.2))              # float
print('5:', mayor("ABC", "ABCD"))
print('6:', mayor("ABC", "ABCA"))
print('7:', mayor(False, True))           # boolean
print('8:', mayor([10, 5, 20], [10, 3]))  # boolean


# --------------------------------
# Manejo de excepciones, ejemplos
# --------------------------------

# Compara dos valores None
try:
  print(mayor(None, None))            # none
except TypeError:
  print('No es posible comparar dos valores none. ¿Por qué?')

# Compara valores de tipo int y string
try:
  print(mayor(4, '¡Hola!'))
except TypeError:
  print('No es posible comparar valores int y string. ¿Por qué?')

