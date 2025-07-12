# accepted 

palabra = input()


char = palabra[0]
contador = 0
char = char.islower()
largo = len(palabra)-1
if(char):
    for i in palabra:
        i = i.isupper()
        if (i):
            contador = contador + 1
    if(largo==contador):
        final = palabra.capitalize()
        print(final)
        exit(0)
        

if palabra.isupper():
    final = palabra.lower()
    print(final)
    exit(0)


if palabra.islower():
    final = palabra.lower()
    print(final)
    exit(0)




print(palabra)