d = {'greg' : 1,'steve' : 2, 'rob' : 3 }
print(d)

# add values 

d['andres'] = 4
print(d)

# lookup keys 

if('greg' in d):
    print(True)

# check value

print(d['greg'])

# loop over the key value pairs

for key,value in d.items():
    print(f'key {key}: val {value}')

# default dict

from collections import defaultdict

default = defaultdict(int) # esto hace que el index se inicialize con el key 2 y val int o list o lo que uno ponga
print(default[2])

#counter

from collections import Counter
string = 'aaaaaabbbbbbbccccccdddddd'
count = Counter(string)
print(count)
# imprime el value y su numero de ocurrenciassss