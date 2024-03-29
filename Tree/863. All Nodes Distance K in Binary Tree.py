"""Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000"""

from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def dfs(node,parent=None):
            if node:
                node.parent = parent
                dfs(node.left,node)
                dfs(node.right,node)

        dfs(root)

        queue = [(target,0)]

        seen = {target}

        while queue:
            if queue[0][1] == k:
                return [node.val for node,d in queue]

            node,d = queue.pop(0)

            for nei in (node.left,node.right,node.parent):
                if nei and nei not in seen:
                    # add nei to seen
                    seen.add(nei)
                    # add nei to queue with distance + 1
                    queue.append((nei,d+1))

        return []

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    print(Solution().distanceK(root,root.left,2))