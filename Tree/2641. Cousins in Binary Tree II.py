"""
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

 

Example 1:


Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
"""
from typing import Optional
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = deque([root])
        levelSum=[]

        while queue:
            curr_level_sum=0
            for _ in range(len(queue)):
                node=queue.popleft()
                curr_level_sum+=node.val

                if node.left:
                    queue.append(node.left)

                if node.right:

                    queue.append(node.right)

            levelSum.append(curr_level_sum)


        queue = deque([(root,root.val)]) # (node, parent_val)
        level=0

        while queue:
            for _ in range(len(queue)):
                node,parent_val=queue.popleft()

                node.val=levelSum[level]-parent_val

                child_sum=0
                if node.left:
                    child_sum+=node.left.val

                if node.right:
                    child_sum+=node.right.val



                if node.left:
                    queue.append((node.left, child_sum))

                if node.right:
                    queue.append((node.right, child_sum))
            level+=1               

        return root
# Time complexity: O(N)


