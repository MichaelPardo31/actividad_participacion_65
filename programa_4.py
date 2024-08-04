#Escribir un programa que determine si un número dado es par o impar.

numero_dado = int(input("Ingrese un numero para saber si es par o impar "))

if numero_dado % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")