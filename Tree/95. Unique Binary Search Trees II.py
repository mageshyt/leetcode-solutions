""""Given an integer n, return all the structurally unique BST's (binary search trees),
 which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]

"""

class Solution:
    def generateTrees(self, n: int):
        
        def helper(left, right):
            # Base cases:
            # If left and right are equal, there's only one node, so return a list with the TreeNode.
            if left == right:
                return [TreeNode(left)]
            
            # If left is greater than right, there are no nodes in the tree, so return a list with None.
            if left > right:
                return [None]

            res = []

            # Try all possible values as the root of the current subtree.
            for val in range(left, right + 1):
                # Generate all possible left subtrees.
                for leftTree in helper(left, val - 1):
                    # Generate all possible right subtrees.
                    for rightTree in helper(val + 1, right):
                        # Create a new root node with the current value and the left and right subtrees.
                        root = TreeNode(val, leftTree, rightTree)
                        # Append the new root node to the result list.
                        res.append(root)

            return res
        
        return helper(1, n)

