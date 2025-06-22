import math

numero = int(input())

validacion = str(numero)
if (validacion.endswith("99")):
    exit(0)

i = numero
numero2 = 0
numero1 = 0

for i in range(i+1,10000):
    numerousar = i
    numerousar = str(numerousar)
    if numerousar.endswith("99"):
        numero1 = int(numerousar)
        break

for i in range(i-1,10,-1):
    numerousar = i
    numerousar = str(numerousar)
    if numerousar.endswith("99"):
        numero2 = int(numerousar)
        break


diferencia1 = numero1 - numero

diferencia2 = numero - numero2

if(numero2 == 0):
    print(numero1)
    exit(0)
if(numero1 == 0):
    print(numero2)
    exit(0)
if (diferencia1 == diferencia2):
    print(numero1)
    exit(0)
if(diferencia1 > diferencia2):
    print(numero2)
    exit(0)
if(diferencia2 > diferencia1):
    print(numero1)
    exit(0)
