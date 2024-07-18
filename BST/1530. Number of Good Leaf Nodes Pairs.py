class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res=0
        def helper(node):
            if not node:
                return []
            # leaf node
            if not node.left and not node.right:
                return [1]

            left=helper(node.left) # left distance from the leaf node
            right=helper(node.right) # right distance from the leaf node

            all_distances= left+right

            for d1 in left:
                for d2 in right:
                    if d1+d2<=distance:
                        self.res+=1

            return [ dist+1 for dist in all_distances if dist+1<distance ]

        helper(root)
        return self.res
