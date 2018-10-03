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