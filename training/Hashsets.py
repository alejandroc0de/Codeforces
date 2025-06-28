s = set()
print(s)

# add to set o(1)
s.add(1)
s.add(2)
s.add(3)

print(s)

# look up 
if 4 not in s:
    print(False)

# remove elements
s.remove(3)
print(s)

# adding a big string 
string = "aaaaaaaabbbbbbbbcccccccddddddd"
set2 = set(string)       # el set no permite duplicados, asi que el set solo tiene 4 letras, abcd.
print(set2)

