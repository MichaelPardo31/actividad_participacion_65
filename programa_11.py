#Crear un programa que genere una lista de números pares entre 1 y 100.
def generar_pares(min,max):
    lista = []
    for numero in range(min, max + 1):
        if numero % 2 == 0:
            lista.append(numero)
    return lista

rango_min = 1
rango_max = 100
lista_pares = generar_pares(rango_min, rango_max)
print(lista_pares)

