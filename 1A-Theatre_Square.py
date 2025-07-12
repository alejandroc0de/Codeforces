# accepted 

# so we use ceiling since we have to cover everything, doesnt matter if it goes over the border.
# nos dice cuantos cuadrados necesitamos para el vertical y el horz, y luego solo multiplicamos

import math
n,m,sizeflag = map(int,input().split(" "))

cuadradosHor = math.ceil((n/sizeflag))
cuadradosVer = math.ceil((m/sizeflag))

resultado = cuadradosHor*cuadradosVer
print(resultado)