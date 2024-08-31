def celsius_fahrenheit  (temperaturac):
    return (temperaturac * 9/5 + 32)
 
temperaturac =float(input("ingrese la temperatura en celsius:"))
resultado = celsius_fahrenheit(temperaturac)
print("su resultado es: " , resultado)