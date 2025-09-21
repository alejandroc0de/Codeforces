price,dollars,toBuy = map(int, input("").split(" "))


total = 0

for i in range(1,toBuy+1):
    total = total + (i*price)
  

pagar = total-dollars
if(pagar>0):
    print(pagar)
else:
    print(0)