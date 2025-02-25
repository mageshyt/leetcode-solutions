"""
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time O(n) and space O(n)
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack=[]

        i,dashes=0,0

        while i < len(traversal):
            if traversal[i]=="-":
                dashes += 1
                i += 1
            else:
                # get all the digits
                j=i

                while j < len(traversal) and traversal[j] != "-":
                    j += 1

                # get the value
                value=int(traversal[i:j])
                node=TreeNode(value)
                while len(stack) > dashes:
                    stack.pop()

                if stack and not stack[-1].left:
                    stack[-1].left=node

                elif stack:
                    stack[-1].right=node

                stack.append(node)

                i=j
                dashes=0

        return stack[0] if stack else None


                 




