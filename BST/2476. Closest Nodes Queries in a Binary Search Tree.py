# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr=[]
        # in order traversal will give us sorted array
        self.inOrder(root,arr)

        ans=[]

        for target in queries:
            minIdx=self.getMinIdx(arr,target)
            maxIdx=self.getMaxIdx(arr,target)
            ans.append([minIdx,maxIdx])

        return ans


    def inOrder(self,root,arr):
        if not root:
            return
        self.inOrder(root.left,arr)
        arr.append(root.val)
        self.inOrder(root.right,arr)

    def getMinIdx(self,arr,target):
        ans=-1
        left=0
        right=len(arr)-1

        while left<=right:
            mid=(left+right)//2
            if arr[mid]==target:
                return arr[mid]
            elif arr[mid]>target:
                right=mid-1

            else:
                ans=arr[mid]
                left=mid+1

        return ans
    
    def getMaxIdx(self,arr,target):
        ans=-1
        left=0
        right=len(arr)-1

        while left<=right:
            mid=(left+right)//2
            if arr[mid]==target:
                return arr[mid]
            elif arr[mid]>target:
                ans=arr[mid]
                right=mid-1
            else:
                left=mid+1

        return ans
    

        