class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build(start, end):
            if start > end:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = inorder.index(val)
            root.right = build(index + 1, end)
            root.left = build(start, index - 1)
            return root

        return build(0, len(inorder) - 1)
