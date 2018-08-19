from binary_tree import *

def has_path_sum(root, _sum):
    if not root:
        return False
    if not root.left and not root.right:
        return _sum == root.val
    return (has_path_sum(root.left, _sum-root.val) or \
            has_path_sum(root.right, _sum-root.val))

if __name__=="__main__":
    root = get_sample_binary_tree()
    print has_path_sum(root, 619)
    print has_path_sum(root, 620)