
# Verificación de Palíndromos

Este proyecto es un programa en Python que verifica si una cadena de texto es un **palíndromo**.

## Funcionalidades

- Comprueba si una palabra o frase es un palíndromo, ignorando mayúsculas, espacios y caracteres especiales.
- Proporciona una interfaz interactiva para ingresar cadenas.
- Incluye pruebas unitarias para garantizar su correcto funcionamiento.

## Uso

### Programa interactivo
Ejecuta el archivo principal en el terminal con el siguiente comando y verás la magia:

python run.py

## Análisis y Pruebas Realizadas

Se desarrollaron pruebas exhaustivas para garantizar el correcto funcionamiento de la función `esPalindromo`:

1. **Casos básicos de palíndromos**: Se prueban palabras simples y comunes como "anilina", "Ana", y frases con espacios intermedios, como "A Santa at NASA".
   
2. **Casos no palíndromos**: Se prueban cadenas como "Hola mundo" y "Python", que no son palíndromos.

3. **Palíndromos con tildes y signos de puntuación**: Se verifica el manejo de caracteres especiales, tildes y signos como en "Luz azul", "Dábale arroz a la zorra el abad", y "¿Acaso hubo búhos acá?".

4. **Casos límite**: Se prueba con cadenas vacías y un solo carácter, que siempre deben considerarse palíndromos (por ejemplo, `""` y `"a"`).

5. **Palíndromos con caracteres especiales y números**: Se evalúan cadenas como "12321", "!@#@@#@!", y combinaciones mixtas de letras y símbolos, verificando que se manejen correctamente.

6. **Casos complejos**: Se prueban frases más complejas con espacios y caracteres especiales, como "A man, a plan, a canal: Panama" y "No 'x' in Nixon".

7. **Entradas inválidas**: Se verifica que la función lance un `TypeError` cuando se pasan entradas no válidas, como `None`, números enteros o listas.

8. **Entradas aleatorias**: Se genera una lista de entradas diversas (cadenas comunes, números, caracteres especiales, etc.) para validar el comportamiento de la función en una variedad de casos posibles.

9. **Combinación de `assertTrue` y `assertEqual`**: Se garantiza que la función devuelva los valores exactos `True` o `False` cuando corresponde. Además, se valida que los resultados coincidan explícitamente con estos valores en casos clave, como "radar" o "python".

Estas pruebas aseguran que la función `esPalindromo` maneje adecuadamente todas las posibles entradas, tanto válidas como inválidas, y que se comporte de manera robusta ante casos de uso comunes y complejos.

Realizado por Daniel César Vargas Holguín
