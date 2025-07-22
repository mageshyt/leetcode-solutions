
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        current_sum = 0
        start= 0 # window start
        path = set()

        for i in range(len(nums)):
            while nums[i] in path :
                path.remove(nums[start])
                current_sum -= nums[start]
                start += 1

            path.add(nums[i])
            current_sum += nums[i]
            maxi = max(maxi, current_sum)

        return maxi if maxi != float('-inf') else 0


        
