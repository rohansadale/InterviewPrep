from linked_list import *
from ll_7_4_overlapping_list import *
from ll_7_3_circular_list import *

def distance(n1, n2):
    dist = 0
    while n1 != n2:
        dist += 1
        n1 = n1.next
    return dist

def overlapping_circular_list(head0, head1):
    root0, root1 = has_cycle(head0), has_cycle(head1)

    if not root0 and not root1:
        return overlapping_no_cycle_list(head0, head1)
    if (root0 and not root1) or (root1 and not root0):
        return None
    
    l0, l1 = distance(head0, root0), distance(head1, root1)
    if l0 > l1:
        head0, head1 = head1, head0
        root0, root1 = root1, root0
    for _ in range(abs(l0-l1)):
        head1 = head1.next
    while head0 is not head1 and head0 is not root0 and head1 is not root1:
        head0, head1 = head0.next, head1.next
    
    if head0 is head1:
        return head0
    return root0