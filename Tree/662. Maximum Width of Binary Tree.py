# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:return None
        queues=[(root,0)]
        max_width=1
        while queues:
            if len(queues) >1 :
                max_width=max(max_width,queues[-1][1] - queues[0][1]+1)
            
            for _ in range(len(queues)):
                node,pos=queues.pop(0)
                if node.left != None:
                    queues.append((node.left,pos*2))
                if node.right != None:
                    queues.append((node.right,pos*2+1))
                    
        return max_width
                    
            
            
            