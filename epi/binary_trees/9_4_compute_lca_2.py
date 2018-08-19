def get_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.parent

def lca(node1, node2):
    depth1, depth2 = get_depth(node1), get_depth(node2)
    if depth1 < depth2:
        node1, node2 = node2, node1
    diff = abs(depth1-depth2)
    while diff:
        node1 = node1.parent
        diff -= 1
    while node1 is not node2:
        node1, node2 = node1.parent, node2.parent
    return node1