# -*- coding: utf-8 -*-

def ordenamientoBurbuja(unaLista):
    for extremo in range(len(unaLista)-1,0,-1):
        for i in range(extremo)
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp


unaLista = [54,26,93,17,77,31,44,55,20]

ordenamientoBurbuja(unaLista)

print(unaLista)


# Ejercicio:
#   Mejorar el algoritmo para que detecte si la lista 
#   ya se encuentra ordenada.
