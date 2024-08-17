peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura * altura)
print("Su IMC es:", imc)
if imc >= 25:
    print("Usted tiene sobrepeso.")
else:
    print("Usted no tiene sobrepeso.")