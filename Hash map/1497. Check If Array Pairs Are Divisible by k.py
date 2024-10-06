from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modFreq = [0] * k

        for num in arr:
            remainder = num % k
            # for negative numbers
            if remainder < 0:
                remainder += k
            modFreq[remainder] += 1

        if modFreq[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if modFreq[i] != modFreq[k - i]:
                return False

        return True

print(Solution().canArrange([1,2,3,4,5,10,6,7,8,9],5)) # True

        
