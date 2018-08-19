from binary_tree import *

def preorder(root):
    s, result = [root], []
    while s:
        x = s.pop()
        if x:
            result.append(x.val)
            s.append(x.right)
            s.append(x.left)
    return result

if __name__ == "__main__":
    root = get_sample_binary_tree()
    tree_traversal(root)
    print
    print preorder(root)
    