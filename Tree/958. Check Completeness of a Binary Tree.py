"""Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation:
 Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:


Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
"""
from collections import *


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # approach: BFS
        queues = deque([root])  # use deque to implement BFS

        while queues:
            node = queues.popleft()
            # if node is None, then all the nodes after this node should be None
            if node:
                queues.append(node.left)  # append left child
                queues.append(node.right)  # append right child
            else:
                break

        # check if all the nodes after the first None node are None
        return all(node is None for node in queues)
