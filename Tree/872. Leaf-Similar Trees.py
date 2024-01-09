"""Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
"""
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,leaf):
            if not node:
                return
            # when node dont have left and right child, it is a leaf
            if not node.left and not node.right:

                leaf.append(node.val)

            dfs(node.left,leaf)
            dfs(node.right,leaf)

        leaf1=[]

        dfs(root1,leaf1)
        leaf2=[]
        dfs(root2,leaf2)

        return leaf1==leaf2

        