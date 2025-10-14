#  binary trees

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)  
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

'''
def pre_order(node):
# Si el nodo es nulo entonces nos devolvemos (recursion)
    if not node:
        return
    print(node)             # procesamos el nodo y luego left y luego right 
    pre_order(node.left)
    pre_order(node.right)
pre_order(A)

print("\n")

def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)
in_order(A)

def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)
pre_order(A) 

'''

'''
lista = []

print("\n")
def pre_order_stack(node):
    stk = [node]
    while stk:
        node = stk.pop()
        lista.append (node.val)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
pre_order_stack(A)

print(sum(lista))

'''


# Check if a value is there using recursion

def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    # si el current node no es el target hacemos
    return search(node.left, target) or search(node.right, target)

print(search(A, 5))