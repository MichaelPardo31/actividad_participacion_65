#Escribir una función que calcule la media aritmética de una lista de números.

def calcular_media(lista):
    suma = sum(lista)
    cantidad = len(lista)
    media = suma / cantidad
    return media

a = [10, 20, 30, 40, 50]
media = calcular_media(a)
print(f"La media aritmética es: {media}")
