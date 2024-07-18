"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.



Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

"""

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def helper(node, path,target):
            if not node :
                return ''

            if node.val==target:
                return path

            path.append('L')
            left_res=helper(node.left, path,target)
            if left_res:
               return left_res
            path.pop()

            path.append('R')

            right_res=helper(node.right, path,target)
            if right_res:
                return right_res
            return ''

        start_path=helper(root, [],startValue)
        dest_path=helper(root, [],destValue)
        i=0

        while i < min(len(start_path),len(dest_path)):
            if start_path[i]!=dest_path[i]:
                break
            i+=1

        return 'U'*(len(start_path)-i)+dest_path[i:][::-1]
