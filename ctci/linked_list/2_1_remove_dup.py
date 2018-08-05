class Node:
    def __init__(self, x):
        self.val = x
        self.next =  None

def print_ll(head):
    while head:
        print head.val,
        head = head.next

# method 1
def remove_duplicates(head):
    if not head:
        return None
    uniques = set()
    n = head
    prev = None
    while n:
        if n.val in uniques:
            prev.next = n.next
        else:
            uniques.add(n.val)
            prev = n
        n = n.next
    return head

# method 2
# Not using buffer
def remove_duplicates_2(head):
    if not head:
        return None
    runner = head
    prev = head
    cur = prev.next
    while cur:
        runner = head
        while runner != cur:
            if runner.val == cur.val:
                prev.next = cur.next
                cur = cur.next
                break
            runner = runner.next
        if runner == cur:
            prev = cur
            cur = cur.next
    return head


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(1)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print_ll(remove_duplicates_2(n1))

