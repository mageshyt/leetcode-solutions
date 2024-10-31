"""
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.

"""
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = {}

        def findHeight(node):
            # base case - for leaf nodes the height is 0
            if not node:
                return 0

            # if we have already calculated the height of the node, return it
            if node.val in height:
                return height[node.val]
            
            # calculate the height of the left and right subtrees
            h=1+max(findHeight(node.left),findHeight(node.right))
            # store the height of the node
            height[node.val]=h
            return h

        res={}

        def dfs(node,depth,max_val):
            if not node:
                return
            res[node.val]=max_val

            dfs(node.left,
                depth+1,
                max(max_val,findHeight(node.right)+depth+1)
                )
            dfs(node.right,
                depth+1,
                max(max_val,findHeight(node.left)+depth+1)
                )

        dfs(root,0,0)

        return [res[q] for q in queries]

