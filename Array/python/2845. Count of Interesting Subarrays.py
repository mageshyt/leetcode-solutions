

from typing import List
from collections import defaultdict
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        count = 0
        mod_count = defaultdict(int)
        mod_count[0] = 1
        equals=0

        for num in nums:
            if num % modulo == k:
                equals += 1

            rem=equals % modulo
            need=(rem-k+modulo) % modulo
            count += mod_count[need]
            mod_count[rem] += 1
        return count


s=Solution()
print(s.countInterestingSubarrays([1,2,3,4,5], 2, 1)) # Output: 4
