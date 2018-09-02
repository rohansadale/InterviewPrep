def lca (node0, node1):
    parents = set()
    while node0 or node1:
        if node0:
            if node0 in parents:
                return node0
            else:
                parents.add(node0)
                node0 = node0.parent
        if node1:
            if node1 in parents:
                return node1
            else:
                parents.add(node1)
                node1 = node1.parent
    return None