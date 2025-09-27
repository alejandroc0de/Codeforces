cases = int(input())

for _ in range(cases):
    usedNumbers = []
    amountNumbers = int(input())
    listaNumbers = list(map(int, input().split(" ")))


    listaNumbers.sort(reverse=True)
    
    ok = True

    for i in range(amountNumbers):
        while (listaNumbers[i]>amountNumbers or (i>0 and listaNumbers[i] in usedNumbers)):
            listaNumbers[i] = listaNumbers[i]//2
        if(listaNumbers[i] == 0):
            ok = False
            break
        usedNumbers.append(listaNumbers[i])
    
    print("YES" if ok else "NO")

