"""
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

 

Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            # current node has node.val coins, left subtree has left coins, right subtree has right coins, so extra_coins is the total coins in the subtree - 1
            extra_coins = node.val+left+right-1
            res[0] += abs(extra_coins)

            return extra_coins

        dfs(root)

        return res[0]

# Complexity Analysis
# The time complexity for this approach is O(N), where N is the number of nodes in the binary tree.
# The space complexity for this approach is O(H), where H is the height of the binary tree.
