class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
       
        ans=0


        def dfs(node):
            if not node:
               return
            if node.val>=low and node.val<=high:
               nonlocal ans
               ans+=node.val

            if node.val>low:
                dfs(node.left)

            if node.val<high:
                dfs(node.right)

        dfs(root)
       
        return ans
       

                
           
            