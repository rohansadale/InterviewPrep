from linked_list import *

def has_cycle(head):
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None

if __name__=="__main__":
    arr = [1,2,3,4,5]
    n1 = create_ll(arr)
    last_node = get_last_node(n1)
    last_node.next = n1.next.next
    root = has_cycle(n1)
    if root:
        print root.val
