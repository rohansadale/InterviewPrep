from binary_tree import TreeNode

def sum_root_to_leaf(root, partial_sum=0):
    if not root:
        return 0
    
    partial_sum = 2*partial_sum + root.val
    if not root.left and not root.right:
        return partial_sum
    return (sum_root_to_leaf(root.left, partial_sum) + \
            sum_root_to_leaf(root.right, partial_sum))

if __name__ == "__main__":
    n1 = TreeNode(1, 'A')
    n2 = TreeNode(0, 'B')
    n3 = TreeNode(1, 'I')
    n1.left, n1.right = n2, n3
    n4 = TreeNode(0, 'C')
    n5 = TreeNode(1, 'F')
    n6 = TreeNode(0, 'I')
    n7 = TreeNode(0, 'O')
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    n8 = TreeNode(0, 'D')
    n9 = TreeNode(1, 'E')
    n10 = TreeNode(1, 'G')
    n11 = TreeNode(0, 'H')
    n4.left, n4.right = n8, n9
    n5.right = n10
    n10.left = n11
    n12 = TreeNode(0, 'K')
    n13 = TreeNode(0, 'P')
    n14 = TreeNode(1, 'L')
    n15 = TreeNode(0, 'N')
    n16 = TreeNode(1, 'M')
    n6.right =  n12
    n7.right = n13
    n12.left, n12.right = n14, n15
    n14.right = n16

    print sum_root_to_leaf(n1)