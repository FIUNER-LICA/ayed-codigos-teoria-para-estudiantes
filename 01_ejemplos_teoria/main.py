# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:06:21 2022

@author: entre todos
"""

# Ctrl + 1: para comentarios

# # Hola mundo
# print('Hola mundo!')

# # Ingresar información
# entrada = input("Por favor, escribe algo: ")

# print(entrada)
# print(type(entrada))

# # Calculadora
# a = float(input("Ingresa un número: "))
# b = float(input("Ingresa otro número: "))

# # print('type(a):', type(a))
# # resultado = a + b
# # print("El resultado es:", resultado)

# # Definición de función "suma y producto"
# def calcular_suma_y_producto(pa, pb):
#     suma = pa + pb
#     prod = pa * pb
#     return suma, prod

# r_sum, r_prod = calcular_suma_y_producto(a, b)

# print("Suma:", r_sum)
# print("Producto:", r_prod)

# Ciclos de control
contador = 0
n = 128
while n > 1:
    n = n//2
    print(n)
    contador += 1

print('contador:', contador)

#  for
print()

# lista = [1, 3, 5, 7, 9]
ini = 1
fin = 9
step = 2
lista = [val**2 for val in range(ini, fin, step)]

for valor in lista:
    print(f'valor: {valor}')


