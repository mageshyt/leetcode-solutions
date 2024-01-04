
from collections import Counter
from typing import List
import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache={}
        def dfs(n):
            if n < 0:
                return float('inf')
            
            if n in [2,3]:
                return 1
            
            if n in cache:
                return cache[n]
            
            ans=min(dfs(n-2),dfs(n-3))+1 # we have tow options: either we can remove 2 or 3 elements
            if ans ==-1:
                return -1
            
            cache[n]=ans
            return ans
        
        counter=Counter(nums)
        res=0
        for k,v in counter.items():
            operations=dfs(v)
            if operations == float('inf'):
                return -1
            else:
                res+=operations
        return res
        
if __name__ == "__main__":
    nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]

    print(Solution().minOperations(nums))
        