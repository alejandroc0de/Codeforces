columnas = int(input(""))
boxes = list(map(int, input("").split(" ")))
boxes.sort()

for i in boxes:
    print(i, end=" ")
exit(0)