from linked_list import *

def reverse_sublist(head, start, finish):
    dummy = sublist_head = head
    for i in range(start-1):
        sublist_head = sublist_head.next
    
    sublist_iter = sublist_head.next
    #print sublist_head.val, sublist_iter.val
    for i in range(finish-start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp
        #print_ll(head)
    return dummy

arr = [11, 3, 5, 7, 8, 10]
head = create_ll(arr)
print "Before - ",
print_ll(head)
head = reverse_sublist(head, 1, 3)
print "After - ",
print_ll(head)