from linked_list import *

def delete_node(node):
    if node.next != None:
        prev = None
        node.val = node.next.val
        node.next = node.next.next

arr = [1,2,3,4,6]
n1 = create_ll(arr)
delete_node(n1.next.next)
print_ll(n1)
