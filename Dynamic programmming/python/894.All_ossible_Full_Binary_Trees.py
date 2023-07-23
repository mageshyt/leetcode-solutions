"""Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
"""
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {
            0: [],        # Base case for 0 nodes (empty tree)
            1: [TreeNode()],  # Base case for 1 node (single node tree)
        }  # map n: list of BST

        def backtrack(n):
            if n in dp:
                return dp[n]
            res = []
            # Number of nodes in the left sub-tree
            for l in range(n):
                r = n - 1 - l  # Number of nodes in the right sub-tree
                leftTree, rightTree = backtrack(l), backtrack(r)

                # Generate all possible combinations of left and right subtrees

                for t1 in leftTree:
                    for t2 in rightTree:
                        res.append(TreeNode(0, t1, t2))

            dp[n] = res
            return res

        return backtrack(n)


                


            

