# accepted

word = input().lower()
largo = word.__len__()
segundalista = []
newlista = []

for i in range(0,largo,1):
    newlista.append(word[i])

lista = ["a","e","i","o","u","y"]
index = 0

for i in range(0,len(newlista),1):
    if (newlista[i] not in lista):
        segundalista.append(newlista[i])

for index in range(0,len(segundalista)*2,2):
    segundalista.insert(index,".")
    index = index + 1

print(*segundalista,sep="")