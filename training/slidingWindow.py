#Find biggest substring not repeating 
letras = 'abcabcaa'
l = 0
longest = 0
sett = set()
r = 0
n = len(letras)

for r in range(n): #Largo string, y R va subiendo

    while letras[r] in sett: # Aqui lo paramos hasta que tengamos algo valido en el set
        sett.remove(letras[l])
        l += 1     #Movemos el L (cola) y removemos del set

    # SI ES VALIDO :
    w = (r - l) + 1 #Formula para saber el largo, +1 SIEMPRE
    longest = max(longest,w) #Sacamos el max so far
    sett.add(letras[r]) #Valido entonces añadimos al set 

print(longest) #R: 3



#Fix lenght, find biggest sum of subarrays size K
nums = [1,12,-5,-6,50,3]
n = len(nums)
k = 4
currentsum = 0
maximoSum = -9999999

for i in range(k): # Calculamos los 4 primeros 
    currentsum += nums[i]
maximoSum = currentsum

for i in range(k,n):
    currentsum += nums[i] #Como le sumamos 1 index mas del array 
    currentsum -= nums[i-k] #Le restamos uno de la cola con la formula
    maximoSum = max(currentsum,maximoSum) #Sacamos max 

print(maximoSum) #R: 51