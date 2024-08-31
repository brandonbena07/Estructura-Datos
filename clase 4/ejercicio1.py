def operaciones_matematicas (N1, N2, operaciones):
    if operaciones == 'suma':
        return N1 + N2
    elif operaciones == 'resta':
        return N1 - N2
    elif operaciones == 'multiplicacion':
        return N1 * N2
    elif operaciones == 'diviSion':
       if N2 == 0:
        return "NO SE PUEDE OPERAR"
       else:
           return N1 / N2
    else:
        return "operacion no valida"
N1 = float (input("INGRESE UN NUMERO:"))
N2 = float (input("INGRESE UN NUMERO:"))
operaciones = input("QUE OPERACIONES DESEA REALIZAR:")

resultado = operaciones_matematicas(N1,N2,operaciones)
print ("SU RESULTADO ES: " , resultado)

    





