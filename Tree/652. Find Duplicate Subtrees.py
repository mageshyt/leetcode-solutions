class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        memo = {}
        res = []

        def dfs(node):
            # base case
            if not node:
                return '#'

            # recursive case
            left = dfs(node.left)
            right = dfs(node.right)

            subTree = left+','+right+','+str(node.val)

            if subTree in memo:
                if memo[subTree] == 1:  # if is appeared 2nd time  add to res
                    res.append(node)

                memo[subTree] += 1  # increase the count

            else:
                memo[subTree] = 1  # mark the node

            return subTree

        dfs(root)
        return res
