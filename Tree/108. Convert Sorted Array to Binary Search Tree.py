"""Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):

        def helper(left, right):
            if left > right:
                # out of boundary
                return None

            mid = (left+right)//2  # get the middle element

            root = TreeNode(nums[mid])  # create a node with the middle element

            # recursively build the left subtree
            root.left = helper(left, mid-1)
            # recursively build the right subtree
            root.right = helper(mid+1, right)

            return root

        return helper(0, len(nums)-1)


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    print(Solution().sortedArrayToBST(nums))
