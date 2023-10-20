import unittest
from texto import Texto

class TestTexto(unittest.TestCase):
    def test_tiene_mayusculas_y_minusculas(self):
        #texto1 = Texto("Hola Mundo")
        #self.assertTrue(texto1.tiene_mayusculas_y_minusculas())

        texto2 = Texto("Hola mundo")
        self.assertTrue(texto2.tiene_mayusculas_y_minusculas())

        #texto3 = Texto("HoLA MUNDO")
        #self.assertTrue(texto3.tiene_mayusculas_y_minusculas())

if __name__ == '__main__':
    unittest.main()