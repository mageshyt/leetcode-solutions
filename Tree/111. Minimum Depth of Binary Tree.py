'''Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
'''


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        # dfs function to find min depth
        def dfs(node,count=0):
            # edge case if node is None return 0
            if not node:
                return 0

            if not node.left:
                return dfs(node.right,count)
            if not node.right:
                return dfs(node.left,count)
            return min(dfs(node.left,count),dfs(node.right,count)) +1


        return dfs(root)
    
    # bfs solution

    def minDepth2(self,root):

        if not root:
            return 0
        
        queue = deque([root])
        count=1
        while queue:
            size=len(queue)

            for _ in range(size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return count+1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            count+=1



        return count
