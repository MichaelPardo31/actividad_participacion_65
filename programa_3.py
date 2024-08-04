#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random
# A = []
# n = random.randint(1, 20)
#
# for i in range(n):
#     A.append(i)
# print(A)

a = [random.randint(1, 100) for i in range(20)]
print(a)