from linked_list import *

def add_nums(node1, node2):
    sum_node = None
    head = None
    carry = 0
    while node1 or node2:
        val = carry
        carry = 0
        if node1:
            val += node1.val
            node1 = node1.next
        if node2:
            val += node2.val
            node2 = node2.next
        temp = Node(val%10)
        if val/10:
            carry = 1
        if sum_node:
            sum_node.next = temp
            sum_node = sum_node.next
        else:
            head = temp
            sum_node = temp
    if carry:
        sum_node.next = Node(carry)
    return head

arr1 = [3,1,5]
arr2 = [5,9,5]
n1 = create_ll(arr1)
n2 = create_ll(arr2)
print_ll(n1)
print_ll(n2)
print "Sum = ",
print_ll(add_nums(n1, n2))
