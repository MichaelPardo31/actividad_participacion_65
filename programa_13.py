#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división.

def operaciones(x,y):
    suma = x+y
    resta = x-y
    multiplicacion = x*y
    division = x/y
    return f"{suma}\n{resta}\n{multiplicacion}\n{division}"

print(operaciones(1,2))
