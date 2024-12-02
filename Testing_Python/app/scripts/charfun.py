import unicodedata

"""
charfun.py
Programa que determina si una cadena proporcionada por el usuario es un palíndromo.
Para ello, se pedirá por teclado al usuario tantas veces como quiera, hasta que escriba la palabra "salir".

Última Modificación: 02/12/2024
Autor: Daniel César Vargas Holguín
"""

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es un palíndromo.
    Ignora espacios, mayúsculas y caracteres no alfanuméricos.
    
    Parámetros:
        cadena (str): La cadena a evaluar.
    
    Retorno:
        bool: True si la cadena es un palíndromo, False en caso contrario.
    """
    # Normalizar la cadena para eliminar tildes y diferencias entre mayúsculas y minúsculas
    cadena = ''.join(
        c for c in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(c) != 'Mn'
    )
    # Eliminar caracteres no alfabéticos y convertir a minúsculas
    cadena = ''.join(c.lower() for c in cadena if c.isalnum())
    # Comparar la cadena con su reverso
    return cadena == cadena[::-1]