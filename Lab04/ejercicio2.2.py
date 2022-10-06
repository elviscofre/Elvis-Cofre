maximo =  0
minimo =  0
while True:
 try:
    numero = input("Ingrese un numero: ")
    if (numero == "salir"):
        break
    else:
     if int(maximo) < int(numero):
        maximo = numero
     if int(minimo) > int(numero):
        minimo = numero
 except:
       print("Error, ingrese valores numericos")

       
print("maximo:", maximo)
print("minimo:", minimo)