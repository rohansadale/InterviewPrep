import collections

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bin_tree_depth_order(root):
    if not root:
        return None
    result = []
    cur_queue = [root]
    while cur_queue:
        result.append([x.val for x in cur_queue])
        cur_queue = [ 
            child 
            for node in cur_queue
            for child in [node.left, node.right] if child
            ]
    return result

def bin_tree_depth_order_2(root):
    if not root:
        return None
    result = []
    cur_queue = collections.deque()
    cur_queue.append(root)
    while cur_queue:
        x = cur_queue.popleft()
        result.append(x.val)
        if x.left:
            cur_queue.append(x.left)
        if x.right:
            cur_queue.append(x.right)
    return result


if __name__ == "__main__":
    n1 = Node(314)
    n2 = n1.left = Node(6)
    n3 = n1.right = Node(6)
    n2.left = Node(271)
    n2.right = Node(561)
    n3.left = Node(2)
    n3.right = Node(22)
    print bin_tree_depth_order(n1)
    print bin_tree_depth_order_2(n1)