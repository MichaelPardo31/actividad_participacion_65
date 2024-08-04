#Crear una función que convierta grados Fahrenheit a grados Celsius.
def fahrenheit_a_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

temperatura_fahrenheit = float(input("Ingrese su temperatura en Fahrenheit para pasarla a celsius: "))
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit}°F es igual a {temperatura_celsius:.2f}")
