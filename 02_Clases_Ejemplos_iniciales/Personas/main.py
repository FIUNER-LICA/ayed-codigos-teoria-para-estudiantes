# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:08:39 2022

@author: jinsfran
"""

from persona import Persona


print('Cantidad personas:', Persona.contador)

persona_1 = Persona('Juan', 'Perez')
persona_2 = Persona('Mariel', 'Rodriguez')
persona_3 = Persona('Susana', 'Reyes')

print('Cantidad personas:', Persona.contador)

personas = [Persona('Pedro', 'Gonzalez')]
personas.append(Persona('Esteban', 'Seyler'))

print('Cantidad personas:', Persona.contador)

personas.pop(0) # se elimina primera persona de la lista
del persona_1

print('Cantidad personas:', Persona.contador)



# HERENCIA:
    # Nos permite REUTILIZAR CÓDIGO 
    # Representa relaciones de tipo "ES UN".

class AlumnoFIUNER(Persona):

    def __init__(self, p_nombre, p_apellido, p_legajo):
        super().__init__(p_nombre, p_apellido)
        self.legajo = p_legajo
        
    def __str__(self):
        cad = super().__str__() + ', '
        cad += str(self.legajo)
        return cad
    

alumno_1 = AlumnoFIUNER('Mario', 'Gonzalez', 1234)

print()
print(alumno_1)


print('Cantidad personas:', Persona.contador)
print('Cantidad personas:', AlumnoFIUNER.contador)


