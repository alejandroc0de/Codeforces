#accepted

# El :: hace que se inverta la secuencia, es un slicing inverso
index = input()
index2 = index[::-1]

# finalmente al correr fuerza bruta, me di cuenta que la posicion 1321 es 1321-1231 asi que solo hay que invertir 
print(index+index2)