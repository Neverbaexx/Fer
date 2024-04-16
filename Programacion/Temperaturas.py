
def celsius_a_fahrenheit_y_Kelvin(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return  kelvin, fahrenheit


# Pedir al usuario que ingrese la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en Celsius: "))

# Convertir Celsius a Fahrenheit usando la función definida anteriormente
fahrenheit, kelvin = celsius_a_fahrenheit_y_Kelvin(celsius)

# Mostrar el resultado
print("La temperatura en Fahrenheit es:", fahrenheit)
print("La temperatura en kelvin es:", kelvin)