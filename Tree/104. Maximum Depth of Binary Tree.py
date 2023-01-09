'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2'''



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: 
            return 0

        def dfs(node,count=0):
            if not node:
                return count
            count+=1

            return max(dfs(node.left,count),dfs(node.right,count))

        return dfs(root)

