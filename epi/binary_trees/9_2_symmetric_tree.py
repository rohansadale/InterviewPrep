from binary_tree import TreeNode

def is_mirror(l_tree, r_tree):
    if not l_tree and not r_tree:
        return True
    elif l_tree and r_tree:        
        return (l_tree.val == r_tree.val) and \
            (is_mirror(l_tree.left, r_tree.right)) and \
            (is_mirror(l_tree.right, r_tree.left))
    return False

def is_symmetric(root):
    if not root:
        return True
    return is_mirror(root.left, root.right)

if __name__ == "__main__":
    n1 = TreeNode(314, 'A')
    n2 = TreeNode(6, 'B')
    n3 = TreeNode(6, 'I')
    n1.left, n1.right = n2, n3
    n4 = TreeNode(271, 'C')
    n5 = TreeNode(2, 'F')
    n6 = TreeNode(2, 'I')
    n7 = TreeNode(271, 'O')
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    print is_symmetric(n1)