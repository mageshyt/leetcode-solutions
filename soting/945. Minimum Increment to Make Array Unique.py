
from collections import Counter
from typing import List
class Solution:
    # Time : O(n) n is the number of elements in the list
    # Space : O(n) n is the number of elements in the list
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res=0

        count=Counter(nums)
        max_num=max(nums)

        for i in range(max_num+len(nums)):
            if count[i]>1:
                count[i+1]+=count[i]-1
                res+=count[i]-1

        return res
    
nums = [3,2,1,2,1,7]
print(Solution().minIncrementForUnique(nums)) # 6
        