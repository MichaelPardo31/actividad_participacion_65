# Escribir una función que calcule el factorial de un número dado.
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = 5
print(f"El factorial de {numero} es {factorial(numero)}")

