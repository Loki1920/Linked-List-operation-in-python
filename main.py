# creating LinkedList Node 

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next 
        
    def __str__(self):
        return f"node {self.data}-->{self.next}"
        


# printing linkedlist value Iteratively
def print_ll(head):
    while head:
        print(head.data)
        head = head.next
        
# count the number of Node 
def count_LL(head):
    c = 0
    while head:
        c+= 1 
        head = head.next 
    print(f"number of node : {c} ")
    
# insert a node at last 
def insert_at_last(head,data):
    if not head:
        return Node(data)
    ptr = head
    while ptr.next:
        ptr = ptr.next
    ptr.next = Node(data)
    return head
    
# insert at front 
def insert_at_front(head,data):
    x = Node(data)
    x.next = head
    return x
    
# 
    
    
a = Node(1,Node(2,Node(3,Node(4))))
print(a)

a = insert_at_last(a,5)
print_ll(a)
count_LL(a)

a = insert_at_front(a,6)
print_ll(a)
count_LL(a)



