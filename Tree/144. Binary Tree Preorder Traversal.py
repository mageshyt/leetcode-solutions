'''Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]'''

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res=[]
        def preOrder(node):
            if not node:
                return
            res.append(node.val)

            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        return res

