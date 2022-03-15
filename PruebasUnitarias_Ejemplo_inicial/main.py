# -*- coding: utf-8 -*-

from modulos.alg_comparacion import mayor
# esta forma de importar evita tener que escribir "alg_comparacion.mayor(param1, param2)" cada vez que se desea invocar a la función "mayor" del módulo "alg_comparacion".

print('1:', mayor("ABC", "ABG"))          # string
print('2:', mayor('ABC', 'ABG'))
print('3:', mayor(4, 7))                  # int
print('4:', mayor(1.5, 0.2))              # float
print('5:', mayor("ABC", "ABCD"))
print('6:', mayor("ABC", "ABCA"))
print('7:', mayor(False, True))           # boolean
print('8:', mayor([10, 5, 20], [10, 3]))  # boolean


