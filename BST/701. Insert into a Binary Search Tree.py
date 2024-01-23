class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        # if val is less than root, then insert in left subtree
        if val < root.val:
            root.left=self.insertIntoBST(root.left,val)
        # if val is greater than root, then insert in right subtree
        else:
            root.right=self.insertIntoBST(root.right,val)
        return root
    