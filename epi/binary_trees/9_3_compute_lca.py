from binary_tree import *

def get_lca(root, node1, node2):
    if not root:
        return None
    
    if root in [node1, node2]:
        return root
    
    left_lca = get_lca(root.left, node1, node2)
    right_lca = get_lca(root.right, node1, node2)    
    if left_lca and right_lca:
        return root
    if left_lca:
        return left_lca
    return right_lca

if __name__ == "__main__":
    root = get_sample_binary_tree()
    n1 = root.left.left
    n2 = root.left.right.right
    print n1.val, n2.val
    lca = get_lca(root, n1, n2)
    #tree_traversal(root)
    print lca.val
