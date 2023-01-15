'''Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104'''


from collections import deque


class Solution:
    def isSubtree(self, root, subRoot) -> bool:

        # lets find the node from the root

        queue = deque()

        queue.append(root)

        contain = []

        while queue:
            pop = queue.popleft()
            if pop.val == subRoot.val:
                contain.append(pop)
            if pop.left:
                queue.append(pop.left)
            if pop.right:
                queue.append(pop.right)

        def helper(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            # if value not match
            if node2.val != node1.val:
                return False

            return helper(node1.left, node2.left) and helper(node1.right, node2.right)

        for node in contain:
            if helper(node, subRoot):
                return True

        return False
