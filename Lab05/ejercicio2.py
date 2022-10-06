try:
    nombre = input("Ingrese el nombre del archivo : ")
    archivo = open(nombre, "r", encoding="UTF-8")

    for linea in archivo:
        print(linea.upper())
except:
    print("Ingrese un archivo existente")