class SinglyNode:

    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    
    # si imprimimos el obj, solo imprime el value 

    def __str__(self):
        return str(self.value)
    

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)


Head.next = A
A.next = B
B.next = C

# asignamos una variable, y luego recorremos la lista con el next (O(n))

curr = Head
while curr:
    print(curr)
    curr = curr.next

# display list

def display(Head):
    curr = Head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(' -> '.join(elements))
# imprime de manera entendible, join le hace glue a los objetos de la lista

display(Head) 

# search node value

def search (head,val):
    curr = head
    while curr:
        if (curr == val):
            print(True)
            return True
        curr = curr.next

    print(False)
    return False

search(Head,9)
 

