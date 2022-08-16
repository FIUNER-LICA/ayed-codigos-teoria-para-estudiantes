# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 08:04:43 2022

@author: jorda
"""

from fraccion import Fraccion

miFraccion = Fraccion(3,5)

f1 = Fraccion(1,4)
f2 = Fraccion(1,2)

f3 = f1 + f2
# f3 = f1.__add__(f2)

f1 = Fraccion(10,4)
f2 = Fraccion(1,2)

f4 = f1 + f2

print('f3 =', f3)
print('f4 =', f4)

