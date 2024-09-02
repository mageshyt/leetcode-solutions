
from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)

        k = k % total

        for i in range(n):
            if chalk[i] > k:
                return i
            k -= chalk[i]

        return 0

# Time: O(n)
# Space: O(1)
print(Solution().chalkReplacer([5,1,5], 22)) # 0
