contador = 0
suma = 0
primerNumero = True
while True:
 try:
    numero = input("Ingrese un número: ")
    if (numero == "salir"):
        break
    else:
     contador = contador + 1
     suma = suma + int(numero)
    if(primerNumero):
        minimo = int(numero)
        maximo = minimo
        primerNumero = False
 except:
    print("Ingrese un valor numerico")


print("Contador:", contador)
print("Suma:", suma)
print("Promedio:", suma/contador)