#accepted

word = input()

# recorremos cada char en word, y lo comparamos con el target en la posicion i
# si es correcto subimos el i en el target, si no, seguimos revisando letras en el word dado

def funcion(word):
    target = "hello"
    i = 0 
    for char in word:
        if i < len(target) and char == target[i]:
            i = i + 1

        if i == len(target):
            return True
    return False

status = funcion(word)
if (status == True):
    print("YES")
else:
    print("NO")