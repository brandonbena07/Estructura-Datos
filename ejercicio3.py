num1 = float(input("Ingrese el primer número: "))
num2= float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, x, /): ")
if operacion == "+":
    resultado = num1+ num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "x":
    resultado = num1 * num2
elif operacion == "/":
    if Y == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
else:
    print("Operación inválida. Por favor ingrese +, -, x, o /.")
    resultado = None  # Asignamos None para indicar que no hay resultado
if resultado is not None:
    print(f"{num1} {operacion} {num2} = {resultado}")