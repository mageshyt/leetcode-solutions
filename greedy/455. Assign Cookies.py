
from typing import List
from collections import Counter
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # 1. sort both lists
        g.sort()
        s.sort()
        # 2. Initialize two pointers
        p1=0
        p2=0

        res = 0

        # 3. Iterate over both lists

        while p1 < len(g) and p2 < len(s):
            if g[p1] <= s[p2]:
                res += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return res
    

if __name__ == "__main__":
    g = [1,2,3]
    s = [1,1]
    print(Solution().findContentChildren(g, s))

