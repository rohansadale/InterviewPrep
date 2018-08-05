from linked_list import *

def nth_to_last(head, n):
    p1 = head
    p2 = head
    while n > 0:
        p2 = p2.next
        n -= 1
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1.val

arr = [1,2,5,6,7]
n1 = create_ll(arr)
print_ll(n1)
print nth_to_last(n1, 4)
