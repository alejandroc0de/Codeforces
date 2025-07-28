rows,goal = map(int, input().split(" "))


contador = 0

for i in range(1,rows+1,1):
    if (goal%i==0)and(goal<i):
        contador = contador + 1 

print(contador)