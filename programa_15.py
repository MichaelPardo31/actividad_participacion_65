#palindromo

def es_palindromo(cadena):
    cadena_normalizada = ''.join(cadena.split()).lower()

    return cadena_normalizada == cadena_normalizada[::-1]

texto = input("Ingrese una cadena de texto: ")

if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
