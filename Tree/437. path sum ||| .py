

class Solution:
    def __init__(self) -> None:
        self.count = 0

    def pathSum(self, root, target) -> int:
        if not root:
            return 0
        self.helper(root, target)

        self.pathSum(root.left, target)
        self.pathSum(root.right, target)

    def helper(self, root, target):
        if not root:
            return

        if root.val == target:
            self.count += 1

        new_target = target - root.val
        self.helper(root.left, new_target)
        self.helper(root.right, new_target)
