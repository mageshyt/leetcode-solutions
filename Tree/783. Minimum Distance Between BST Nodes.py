"""Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1"""


class Solution:
    def minDiffInBST(self, root) -> int:

        prev = -float('inf')  # previous node

        res = float('inf')  # result

        def dfs(root):
            # inorder traversal
            if root.left:
                dfs(root.left)

            nonlocal prev, res
            res = min(res, root.val - prev)
            prev = root.val

            if root.right:

                dfs(root.right)

        dfs(root)

        return res
