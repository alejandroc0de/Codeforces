class DoublyNode:
    def __init__(self,value,next=None,prev=None):
        self.value = value
        self.next = next
        self.prev = next

    def __str__(self):
        return(str(self.value))
    
# tanto el head y el tail apuntan a lo mismo

head = tail = DoublyNode(1)
print(head)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print('<->'.join(elements))

# inserta al inicio
def insert_at_beg(head,tail,value):
    new_node = DoublyNode(value,next=head)
    head.prev = new_node
    return new_node,tail

head, tail = insert_at_beg(head,tail,3)

display(head)