from linked_list import *

def overlapping_no_cycle_list(head1, head2):
    l1, l2 = len_ll(head1), len_ll(head2)
    if l1 > l2:
        head1, head2 = head2, head1
    for _ in range(abs(l2-l1)):
        head2 = head2.next
    while head1 and head2 and head1 is not head2:
        head1 = head1.next
        head2 = head2.next
    return head1

if __name__ == "__main__":
    arr1 = [0, 1, 2]
    head1 = create_ll(arr1)
    arr2 = [5,6]
    head2 = create_ll(arr2)
    n = get_last_node(head2)
    n.next = head1.next
    print "First list",
    print_ll(head1)

    print "Second list",
    print_ll(head2)
    output = overlapping_no_cycle_list(head1, head2)
    print "Overlapping node - ",
    if output:
        print output.val
    else:
        print "None"