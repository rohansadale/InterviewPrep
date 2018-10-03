## Traversal

### Inorder Tree Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

* Recursive Approach
    ```python
    class Solution(object):
        def inorderTraversal(self, root):
            result = []
            self.helper(root, result)
            return result
        
        def helper(self, node, result):
            if not node:
                return 
            self.helper(node.left, result)
            result.append(node.val)
            self.helper(node.right, result)
    ```
* Iterative Approach
    ```python
    class Solution(object):
        def inorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if not root:
                return []
            stack, result = [], []        
            while True:            
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    if not stack:
                        return result
                    root = stack.pop()
                    result.append(root.val)
                    root = root.right
    ```

### Preorder Tree Traversal
* Recursive Approach
    ```python
    class Solution(object):
        def preorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            result = []
            self.helper(root, result)
            return result
        
        def helper(self, root, result):
            if not root:
                return
            result.append(root.val)
            self.helper(root.left, result)
            self.helper(root.right, result)
    ```
* Iterative Approach
    ```python
    class Solution(object):
        def preorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            stack, result = [], []
            while True:
                if root:
                    result.append(root.val)
                    stack.append(root)
                    root = root.left
                else:
                    if not stack:
                        return result
                    root = stack.pop()
                    root = root.right
    ```

### Postorder Tree Traversal
* Recursive Approach
    ```python
    class Solution(object):
        def postorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            result = []
            self.helper(root, result)
            return result
        
        def helper(self, root, result):
            if not root:
                return
            self.helper(root.left, result)
            self.helper(root.right, result)
            result.append(root.val)
    ```
* Iterative Approach
    *  Using two stacks

        ```python
        class Solution(object):
            def postorderTraversal(self, root):
                """
                :type root: TreeNode
                :rtype: List[int]
                """
                if not root:
                    return []
                stack, result = [root], []
                while stack:
                    x = stack.pop()
                    result.append(x.val)
                    if x.left:
                        stack.append(x.left)
                    if x.right:
                        stack.append(x.right)
                return result[::-1]
        ```
    * Using one stack
        ```python
        class Solution(object):
        def postorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if not root:
                return []
            stack, result = [], []        
            while True:
                while root:
                    if root.right:
                        stack.append(root.right)
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                if len(stack) and root.right == stack[-1]:
                    stack.pop()
                    stack.append(root)
                    root = root.right
                else:
                    result.append(root.val)
                    root = None
                if not stack:
                    return result
        ```

### Level Order Traversal (BFS)
  * Print all levels separately
    ```python
    class Solution(object):
        def levelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            if not root:
                return []
            stack, result = [root],[]
            while stack:
                temp = []
                level_data = []
                for node in stack:
                    level_data.append(node.val)
                    if node.left:
                        temp.append(node.left)                
                    if node.right:
                        temp.append(node.right)
                stack = temp
                result.append(level_data)
            return result
    ```
    ```bash
    # Output
    [
        [3],
        [9,20],
        [15,7]
    ]
    ```