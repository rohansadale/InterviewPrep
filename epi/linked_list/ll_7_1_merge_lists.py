from linked_list import *

def merge_sorted_lists(head1, head2):
    head = tail = Node(0)
    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    if head1 or head2:
        tail.next = head1 or head2
    return head.next

arr1 = [2, 5, 7]
arr2 = [3, 11]
head1 = create_ll(arr1)
head2 = create_ll(arr2)
head = merge_sorted_lists(head1, head2)
print_ll(head)