"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
"""

from collections import *


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # we are going to use queue to traverse the tree

        queue = deque()

        queue.append(p)  # append the root of p
        queue.append(q)  # append the root of q

        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()

            # if both nodes are None, continue
            if not node1 and not node2:
                continue

            # if only one of the nodes is None, return False
            if not node1 or not node2:
                return False

            # if the values of the nodes are not equal, return False

            if node1.val != node2.val:
                return False

            # append the left child of node1 and node2
            queue.append(node1.left)
            queue.append(node2.left)

            # append the right child of node1 and node2
            queue.append(node1.right)

            queue.append(node2.right)

        return True
    
    # solution 2 - dfs

    # Time : O(n) | Space : O(n)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        cache={}

        def dfs(p,q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val!=q.val:
                return False
            
            if (p,q) in cache:
                return cache[(p,q)]
            
            cache[(p,q)]=dfs(p.left,q.left) and dfs(p.right,q.right)

            return cache[(p,q)]
        
        return dfs(p,q)
    

