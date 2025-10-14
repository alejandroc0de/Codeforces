#Create a hashmap
d = {'greg' : 1,'steve' : 2, 'rob' : 3 }
# add values 
d['andres'] = 4
print(d)
#R: {'greg': 1, 'steve': 2, 'rob': 3, 'andres': 4}


# lookup keys 
if('greg' in d):
    print(True)
    #R: True or (if Not in)


# check value
print(d['greg'])
#Prints the value for greg 


# loop over the key value pairs
for key,value in d.items():
    print(f'key {key}: val {value}')
#R : key greg: val 1 key steve: val 2 key rob: val 3 key andres: val 4


# default dict
from collections import defaultdict

default = defaultdict(list) # Hace que si llamamos un index ese index se inicialize con el arg (list,int..)
default[2]
#R: defaultdict(list,{ 2:[] })      Crea una lista en cada index al que llamemos 

#counter
from collections import Counter
string = 'aaaaaabbbbbbbccccccdddddd'
count = Counter(string)
print(count)
# imprime el value y su numero de ocurrenciassss
#R: Counter({'b': 7, 'a': 6, 'c': 6, 'd': 6})