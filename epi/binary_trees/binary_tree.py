class TreeNode:
    def __init__(self, x, text=None):
        self.val = x
        self.text = text
        self.left = None
        self.right = None

def get_sample_binary_tree():
    n1 = TreeNode(314, 'A')
    n2 = TreeNode(6, 'B')
    n3 = TreeNode(6, 'I')
    n1.left, n1.right = n2, n3
    n4 = TreeNode(271, 'C')
    n5 = TreeNode(561, 'F')
    n6 = TreeNode(2, 'I')
    n7 = TreeNode(271, 'O')
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    n8 = TreeNode(28, 'D')
    n9 = TreeNode(0, 'E')
    n10 = TreeNode(3, 'G')
    n11 = TreeNode(17, 'H')
    n4.left, n4.right = n8, n9
    n5.right = n10
    n10.left = n11
    n12 = TreeNode(1, 'K')
    n13 = TreeNode(28, 'P')
    n14 = TreeNode(401, 'L')
    n15 = TreeNode(257, 'N')
    n16 = TreeNode(641, 'M')
    n6.right =  n12
    n7.right = n13
    n12.left, n12.right = n14, n15
    n14.right = n16
    return n1

def tree_traversal(root):
    if root:
        # Preorder
        print root.val,
        tree_traversal(root.left)
        #print "Inorder - ", root.val
        tree_traversal(root.right)
        #print "Postorder - ", root.val

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

if __name__ == "__main__":
    root = get_sample_binary_tree()
    tree_traversal(root)
    print
    print "Height of Tree =",height(root)