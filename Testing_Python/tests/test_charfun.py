# test_charfun.py

import sys
import os

# Agrega el directorio raíz al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
import random
import string
from app.scripts.charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):
    # Casos básicos de prueba con palabras simples y palíndromos comunes
    def test_palindromos_simples(self):
        self.assertTrue(esPalindromo("anilina"))  # Palíndromo básico
        self.assertTrue(esPalindromo("Ana"))  # Mayúsculas y minúsculas
        self.assertTrue(esPalindromo("A Santa at NASA"))  # Espacios intermedios

    # Casos de prueba para palabras/frases que no son palíndromos
    def test_no_palindromos(self):
        self.assertFalse(esPalindromo("Hola mundo"))  # Frase común
        self.assertFalse(esPalindromo("Python"))  # Palabra común no palíndroma

    # Palíndromos que incluyen tildes y signos de puntuación
    def test_palindromos_con_tildes(self):
        self.assertTrue(esPalindromo("Luz azul"))  # Palíndromo con espacios
        self.assertTrue(esPalindromo("Dábale arroz a la zorra el abad"))  # Con tildes
        self.assertTrue(esPalindromo("¿Acaso hubo búhos acá?"))  # Con signos de interrogación

    # Casos límite: cadenas vacías o con un solo carácter
    def test_cadena_vacia(self):
        self.assertTrue(esPalindromo(""))  # Una cadena vacía se considera palíndroma
        self.assertTrue(esPalindromo("a"))  # Un solo carácter es siempre un palíndromo

    # Palíndromos que incluyen caracteres especiales o números
    def test_caracteres_especiales(self):
        self.assertTrue(esPalindromo("12321"))  # Palíndromo numérico
        self.assertFalse(esPalindromo("12345"))  # No palíndromo numérico
        self.assertTrue(esPalindromo("!@#@@#@!"))  # Palíndromo de caracteres especiales
        self.assertFalse(esPalindromo("!@#abc#@!"))  # Mezcla de caracteres y letras no palíndroma

    # Casos extremos con mezcla de mayúsculas, espacios y caracteres especiales
    def test_palindromos_complejos(self):
        self.assertTrue(esPalindromo("A man, a plan, a canal: Panama"))  # Palíndromo famoso
        self.assertTrue(esPalindromo("No 'x' in Nixon"))  # Palíndromo con comillas
        self.assertFalse(esPalindromo("Esto no es un palíndromo"))  # Frase larga no palíndroma

    # Casos inválidos o entrada inesperada
    def test_entrada_invalida(self):
        with self.assertRaises(TypeError):  # Debe lanzar un error si no se pasa una cadena
            esPalindromo(None)
        with self.assertRaises(TypeError):  # Debe lanzar un error si se pasa un número
            esPalindromo(12345)
        with self.assertRaises(TypeError):  # Listas no deberían ser válidas
            esPalindromo(["a", "n", "a"])
    
    def test_random_inputs(self):
        # Lista de entradas random para probar
        entradas_random = [
            "abracadabra",  # Una palabra común
            "12321",  # Número como cadena (palíndromo)
            "12345",  # Número como cadena (no es palíndromo)
            "!@#$%^&*()",  # Solo caracteres especiales
            None,  # Un valor nulo
            12321,  # Número entero (no válido, debe lanzar un error)
            ["a", "n", "a"],  # Lista (no válido, debe lanzar un error)
        ]

        for entrada in entradas_random:
            if isinstance(entrada, str):  # Si es una cadena, es válida
                # Normaliza la cadena como lo haría esPalindromo
                entrada_normalizada = ''.join(c.lower() for c in entrada if c.isalnum())
                es_palindromo = entrada_normalizada == entrada_normalizada[::-1]
                self.assertEqual(esPalindromo(entrada), es_palindromo)
            else:  # Si no es cadena, debe lanzar un error
                with self.assertRaises(TypeError):
                    esPalindromo(entrada)
    
    def test_equals_and_true_combination(self):
        # Palíndromos válidos: asegúrate de que el resultado sea exactamente True
        self.assertTrue(esPalindromo("radar"))
        self.assertEqual(esPalindromo("radar"), True)  # Verifica que sea exactamente True

        # No palíndromos válidos: asegúrate de que el resultado sea exactamente False
        self.assertFalse(esPalindromo("python"))
        self.assertEqual(esPalindromo("python"), False)  # Verifica que sea exactamente False

        # Cadenas con espacios y mayúsculas que son palíndromos
        self.assertTrue(esPalindromo("A man a plan a canal Panama"))
        self.assertEqual(esPalindromo("A man a plan a canal Panama"), True)

        # Casos inválidos que deben fallar con TypeError
        with self.assertRaises(TypeError):
            esPalindromo(12321)  # Número como entrada

if __name__ == "__main__":
    unittest.main()