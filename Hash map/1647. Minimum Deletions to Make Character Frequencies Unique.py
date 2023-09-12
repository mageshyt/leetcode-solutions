from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        
        collect = Counter(s)

        freq = set()

        res = 0

        for key, val in collect.items():

            while val > 0 and val in freq:
                val -= 1
                res += 1

            freq.add(val)

        return res
    

s=Solution()

print(s.minDeletions("aaabbbcc"))