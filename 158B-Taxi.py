from collections import Counter
grupos = int(input())
niños = list(map(int, input().split()))

counter = Counter(niños)
taxis = 0


taxis = taxis + counter[4]
counter[4] = 0

while counter[3]>=1:
    if(counter[3]>=1 and counter[1]==0):
        taxis = counter[3]+taxis
        counter[3] = 0
        break
    while(counter[1]>0 and counter[3]>0):
        taxis = taxis + 1
        counter[3] = counter[3] -1
        counter[1] = counter[1] -1
while counter[2]>1:
    taxis = taxis + 1
    counter[2] = counter[2]-2
while counter[2]==1:
    if(counter[2]==1 and counter[1]<2>0):
        taxis = taxis + 1
        counter[2] = 0
        counter[1] = 0
    while(counter[1]==2):
        taxis = taxis + 1
        counter[2] = counter[2]-1
        counter[1] = counter[1]-2
while(counter[1]<4 and counter[1]>0):
    taxis = taxis + 1
    counter[1] = 0
while(counter[1]>0):
    taxis = counter[1]//4
    counter[1]=0
print(taxis)

