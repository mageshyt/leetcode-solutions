
from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res=[]

        for window in range(0,len(nums),3):

            if nums[window+2] - nums[window] > k:
                print(">> ",nums[window:window+3])
                return  []
            res.append(nums[window:window+3])


        return res
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res=[]

        windowStart=0

        for windowEnd in range(1,len(nums)+1):
            if windowEnd - windowStart ==3:
                subArray=nums[windowStart:windowEnd]
                diff=max(subArray)-min(subArray)
                if diff <= k:
                    res.append(subArray)
                    windowStart=windowEnd
                else:
                    return []

        return res

s=Solution()
print(s.divideArray([1,3,3,2,7,3],3))
        