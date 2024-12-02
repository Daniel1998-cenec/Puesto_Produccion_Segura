from app.scripts.charfun import esPalindromo

def main():
    while True:  # Inicia un bucle infinito que seguirá ejecutándose hasta que el usuario escriba "salir".
        entrada = input("Introduce una cadena de texto (escribe 'salir' para terminar): ")  
        # Pide al usuario que introduzca una cadena de texto.

        if entrada.lower() == "salir":  
            # Convierte la entrada a minúsculas y verifica si es "salir".
            print("Programa terminado.")  
            # Si el usuario escribió "salir", muestra este mensaje.
            break  
            # Rompe el bucle y finaliza el programa.

        if esPalindromo(entrada):  
            # Llama a la función `esPalindromo` para verificar si la entrada es un palíndromo.
            print("La cadena es palíndroma.")  
            # Si es un palíndromo, muestra este mensaje.
        else:
            print("La cadena NO es palíndroma.")  
            # Si no es un palíndromo, muestra este mensaje.

if __name__ == "__main__":  
    main()  
    # Este bloque asegura que el código solo se ejecute si el archivo se ejecuta directamente
    # (y no si es importado como un módulo en otro archivo).