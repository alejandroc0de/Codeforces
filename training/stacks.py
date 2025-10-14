# Stack(Last in First out)

stack = []
stack.append(5)
stack.append(4)
stack.append(3)
print(stack)
#R : [5, 4, 3]

#Pop from stack (last value)
x = stack.pop() # para saber que borramos 
print(x)
print(stack)
#R: 3    [5, 4]

# ask top one O(1)

print(stack[-1])
#R: 4

# ask if stack is empty ot not 
if stack:
    stack.pop()
else:
    print("Nothing on stack")
