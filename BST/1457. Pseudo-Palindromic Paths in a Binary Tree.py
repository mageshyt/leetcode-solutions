class Solution:
    # Time: O(n) | Space: O(n)
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        cache={}
        odd=0
        res=[0]

        def dfs(node):
            nonlocal odd
            if not node:
                return
            cache[node.val]=cache.get(node.val,0)+1
            oddChange=1 if cache[node.val]%2 else -1
            odd+=oddChange
            if not node.left and not node.right:
                if odd<=1:
                    res[0]+=1
            else:
                dfs(node.left)
                dfs(node.right)
            odd-=oddChange
            cache[node.val]-=1
        dfs(root)
        return res[0]
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # Time: O(n) | Space: O(1)
        def dfs(node,odd):
            if not node:
                return 0
            odd^=1<<node.val
            if not node.left and not node.right:
                return 1 if odd & (odd-1)==0 else 0
            return dfs(node.left,odd)+dfs(node.right,odd)
        
        return dfs(root,0)