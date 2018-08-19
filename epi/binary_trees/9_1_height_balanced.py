from binary_tree import *

class Height:
    def __init__(self):
        self.height = 0

def is_balanced(root, height):
    if not root:
        return True
        
    l_height, r_height = Height(), Height()
    l = is_balanced(root.left, l_height)
    r = is_balanced(root.right, r_height)

    height.height = 1 + max(l_height.height, r_height.height)
    if abs(l_height.height - r_height.height) <= 1:
        return l and r
    return False

if __name__ == "__main__" :
    root = get_sample_binary_tree()
    print is_balanced(root, Height())
