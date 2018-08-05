from linked_list import *

def get_circular_ll(node):
    p1 = node
    p2 = node.next
    while p1 and p2 and p1 != p2:
        p1 = p1.next
        p2 = p2.next.next
    return p1    

# Method 1
def circular_head(node):
    p1 = node
    temp = get_circular_ll(node)
    while True:
        p2 = temp.next
        while p1 != p2 and p2 != temp:
            p2 = p2.next
        if p1 == p2:
            return p1
        p1 = p1.next

# Method 2 https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/ 
def circular_head_2(node):
    slow = node
    fast = node
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast:
        return None
    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


arr = [1,2,3,4,5]
n1 = create_ll(arr)
last_node = get_last_node(n1)
last_node.next = n1.next.next
#cir_head = circular_head(n1)
cir_head = circular_head_2(n1)
print cir_head.val