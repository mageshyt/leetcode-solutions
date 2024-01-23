from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[0,0]

        for n in nums:
            num=abs(n)
            if nums[num-1]<0:
                res[0]=num
            else:
                nums[num-1]=-nums[num-1]

        for i in range(len(nums)):
            if nums[i]>0:
                res[1]=i+1
                break
        return res