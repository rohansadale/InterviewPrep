from binary_tree import *

def inorder(root):
    s, result = [], []
    while s or root:
        if root:
            s.append(root)
            root = root.left
        else:
            x = s.pop()
            result.append(x.val)
            root = x.right
    return result

if __name__ == "__main__":
    root = get_sample_binary_tree()
    print inorder(root)