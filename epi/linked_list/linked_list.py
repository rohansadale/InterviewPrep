class Node:
    def __init__(self, x):
        self.val = x
        self.next =  None

def print_ll(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print arr

def create_ll(arr):
    if not arr:
        return None
    n = len(arr)
    head = Node(arr[0])
    temp = head
    for i in range(1,n):
        temp.next = Node(arr[i])
        temp = temp.next
    return head

def get_last_node(node):
    while node.next:
        node = node.next
    return node

def len_ll(node):
    count = 0
    while node:
        count += 1
        node = node.next
    return count