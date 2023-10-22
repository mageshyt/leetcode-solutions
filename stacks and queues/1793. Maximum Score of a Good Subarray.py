
from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # score  can be calculated as min(nums[i:j+1])*(j-i+1)
        left=k
        right=k
        # logic :
        """
        we will start from k and move left and right pointers to optimally to increase the score
        """
         
        res=nums[k]

        curr_min=nums[k]

        while left>0 or right<len(nums)-1:

            # if left is 0, we can only move right
            if left==0:
                right+=1

            # if right is len(nums)-1, we can only move left
            elif right==len(nums)-1:
                left-=1

            # if left and right are not at the ends, we will move the pointer which will increase the score
            elif nums[left-1]>nums[right+1]:
                left-=1

            else:
                right+=1

            curr_min=min(curr_min,nums[left],nums[right])

            res=max(res,curr_min*(right-left+1))

        return res
    

   
