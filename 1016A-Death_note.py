# solved 
days,maxNames = map(int, input().split(" "))
numberNamesDay = list(map(int, input().split(" ")))
modulo = 0
pages = []
sumaday = 0

for names in numberNamesDay:
    names = names + modulo
    sumaday = names
    pasarPagina = names // maxNames
    modulo = names % maxNames
    pages.append(pasarPagina)


for x in pages:
    print(x,end=" ")


