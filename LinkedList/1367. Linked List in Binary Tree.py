"""
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.
"""

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return head.val == root.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        
        if not root:
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


# Time complexity: O(N*M)
# Space complexity: O(N)
