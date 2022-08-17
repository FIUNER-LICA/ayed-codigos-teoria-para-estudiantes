# -*- coding: utf-8 -*-

import unittest
import modulos.alg_comparacion as alg


class Test_Alg_Comparacion(unittest.TestCase):
    
    def setUp(self):
        # Las siguientes dos variables estarán disponibles en 
        # todos los tests.
        self.una_lista = [1, 2, 3, 3, 4]
        self.otra_lista = [1, 2, 4, 0, 0]
        # print("Se corre setUp...")
    
    def test_alg_mayor_numbers(self):
        self.assertEqual(alg.mayor(4,7), 7)
    
    def test_alg_mayor_strings(self):
        self.assertEqual(alg.mayor("ABG","ABC"), "ABG")

    def test_alg_mayor_listas(self):
        resultado = alg.mayor(self.una_lista, self.otra_lista)
        self.assertEqual(resultado, self.otra_lista)
    
    def tearDown(self):
        # print("Se corre tearDown...\n")
        pass
    
if __name__ == "__main__":
    unittest.main()
