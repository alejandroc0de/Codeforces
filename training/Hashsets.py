#Create a hashset
s = set()
# add to set o(1)
s.add(1)
s.add(2)
s.add(3)
print(s)
#R: {1, 2, 3}


# look up 
if 4 not in s:
    print(False)
    #R: False

# remove elements
s.remove(3)
print(s)
#R: {1, 2}


# adding a big string 
string = "aaaaaaaabbbbbbbbcccccccddddddd"
set2 = set(string)       # el set no permite duplicados, asi que el set solo tiene 4 letras, abcd. Mucho mas rapido
print(set2)
#R: {'d', 'a', 'b', 'c'}