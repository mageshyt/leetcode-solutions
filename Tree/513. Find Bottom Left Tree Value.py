class Solution:
    # Time : O(n) | Space : O(n)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
    
    def  findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level):
            if not node:
                return
            if level>self.max_level:
                self.max_level=level
                self.result=node.val
            dfs(node.left,level+1)
            dfs(node.right,level+1)

        self.max_level=0
        self.result=0

        dfs(root,1)

        return self.result
    
    