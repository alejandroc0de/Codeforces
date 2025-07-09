# accepted 

player = (input())

contador = 0
contador0 = 0

for i in player:
    while contador<7 and contador0<7:
        if(i == '1'):
            contador = contador + 1
            contador0 = 0
            break
        else:
            contador = 0
            contador0 = contador0 + 1
            break
          
if(contador0>6 or contador>6):
    print("YES")
else:
    print("NO")


# 1000000001
