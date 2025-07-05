# Stack

stack = []
stack.append(5)
stack.append(4)
stack.append(3)
print(stack)

#Pop from stack (last value)

x = stack.pop() # para saber que borramos 
print(x)
print(stack)

# ask top one O(1)

print(stack[-1])

# ask if in stack

if stack:
    stack.pop()
else:
    print("Nothing on stack")
