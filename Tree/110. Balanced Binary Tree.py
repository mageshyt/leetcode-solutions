'''Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root) -> bool:

        if not root:
            return True

        def dfs(node):
            # base case
            if not node:
                return 0

            # recursive case
            left = dfs(node.left)  # left height
            right = dfs(node.right)  # right height

            # if left or right is -1 then return -1 because we already know that tree is not balanced
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node1.right = node3

node2.left = node4


if __name__ == "__main__":
    print(Solution().isBalanced(node1))
