# Escribir una función que calcule el área de un círculo dado su radio.
import math


def area_circulo(radio):
    area = math.pi*radio**2
    return area

radio = int(input("Ingrese el radio: "))
print(area_circulo(radio))