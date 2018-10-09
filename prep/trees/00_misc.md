## Miscellaneous

### Height of Binary Tree

  * Maximum Height/Depth of a Binary Tree
    ```python
    class Solution(object):
        def maxDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None:
                return 0        
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    ```

  * Minimum Depth of a Binary Tree
    * The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    ```python
    class Solution(object):
        def minDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None:
                return 0
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if left == 0 or right == 0:
                return 1 + left + right
            return 1 + min(left, right)
    ```

  * Maximum Depth of a n-ary Tree
    ```python
    class Solution(object):
        def maxDepth(self, root):
            """
            :type root: Node
            :rtype: int
            """
            if not root:
                return 0
            stack = [root]
            depth = 0
            while stack:
                temp = []
                depth += 1
                for node in stack:
                    for child in node.children:
                        temp.append(child)
                stack = temp
            return depth
    ```

### Symmetric

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
          return True
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self, left, right):
        if not left and not right:
          return True
        if not left or not right:
          return False
        
        if left.val == right.val:
          return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)
        
        return False
```

### Validate BST

*   Recursive
    ```python
    class Solution(object):
        def __init__(self):
            self.prev = None
            
        def isValidBST(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            if not root:
                return True
            if not self.isValidBST(root.left):
                return False
            if self.prev and self.prev.val >= root.val:
                print self.prev.val
                return False
            self.prev = root
            return self.isValidBST(root.right)
    ```

*   Iterative
    ```python
    class Solution(object):
        def isValidBST(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            if not root:
                return True
            stack = []
            prev = None
            while True:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    if not stack:
                        return True
                    root = stack.pop()
                    if prev and prev.val >= root.val:
                        return False
                    prev = root
                    root = root.right
    ```

### Right side view of the Binary Tree

*   Iterative (Level-order)
    ```python
    class Solution(object):
        def rightSideView(self, root):
            if not root:
                return []
            
            stack, result = [root], []        
            while True:
                temp = []
                result.append(stack[-1].val)
                for node in stack:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                stack = temp
                if not stack:
                    break
            return result
    ```

* Recursive
    ```python
    class Solution(object):
        def rightSideView(self, root):
            self.max_depth = 0        
            if not root:
                return []   
            result = []
            self.right_side_helper(root, 1, result)
            return result
        
        def right_side_helper(self, root, depth, result):
            if not root:
                return        
            if self.max_depth < depth:
                result.append(root.val)
                self.max_depth = depth
            self.right_side_helper(root.right, depth+1, result)
            self.right_side_helper(root.left, depth+1, result)
    ```

### Check if Binary Tree is balanced

*   O(n**2) solution
    ```python
    class Solution(object):
        def isBalanced(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            def depth(node):
                if not node:
                    return 0
                return 1 + max(depth(node.left), depth(node.right))
            
            if not root:
                return True
            left = depth(root.left)
            right = depth(root.right)
            if abs(left-right) <= 1 :
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            return False
    ```
*   O(n) solution
    ```python
    class Solution(object):
        def isBalanced(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            def depth(node):
                if not node:
                    return 0
                left = depth(node.left)
                if left == -1:
                    return -1
                right = depth(node.right)
                if right == -1:
                    return -1
                if abs(left-right) > 1:
                    return -1
                return max(left, right) + 1
                
            if not root:
                return True
            return depth(root) != -1
    ```