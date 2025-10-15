# Queues ( First in First out )
from collections import deque
q = deque()

# Enqueue  O(1)
q.append(5)
q.append(6)
q.append(7)
q.append(8)
print(q)
# R: deque([5, 6, 7, 8])


# Deque (Pop Left) - remove from left - O(1) - First in, First out - 
# Important to use LEFT, pop alone will do LAST index
x = q.popleft()
print(x)
print(q)

# peek from left side O(1) - Check what is on the left ready to come out
print(q[0])

# peek from right side O(1) - Check what is last to come out on the right 
print(q[-1])
