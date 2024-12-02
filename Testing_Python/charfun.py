# test_charfun.py
import unittest
from charfun import es_palindromo

class TestCharFun(unittest.TestCase):
    """
    Clase para probar la función es_palindromo.
    """
    def test_palindromo_simple(self):
        self.assertTrue(es_palindromo("Anita lava la tina"))
    
    def test_no_palindromo(self):
        self.assertFalse(es_palindromo("Esto no es un palíndromo"))
    
    def test_palindromo_con_tildes(self):
        self.assertTrue(es_palindromo("Árbol solórba"))

    def test_palindromo_vacio(self):
        self.assertTrue(es_palindromo(""))

    def test_palindromo_caracteres_especiales(self):
        self.assertTrue(es_palindromo("A man, a plan, a canal, Panama"))

if __name__ == "__main__":
    unittest.main()