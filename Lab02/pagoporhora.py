# Tecnologia e Innovacion en Tecnologia Agricola (TEA)
#
horas = input("horas trabajadas? ")
valorporhora = input("valor por hora? ")

# se utiliza la conversión de tipo a int
# sino se hace la conversion existira error porque trata de multiplicar strings
total = int(horas) * int(valorporhora)
print("Usted recibira un total de12:")
print(total)

# solo falta imprimir el tipo