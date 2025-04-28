from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count=0

        n=len(nums)
        left=0
        sum=0

        for right in range(n):
            sum+=nums[right]
            while left<=right and (sum*(right-left+1))>=k:
                sum-=nums[left]
                left+=1
            count+=right-left+1


        return count
 
s=Solution()
print(s.countSubarrays([2,1,4,3,5], 10)) # Output: 6
