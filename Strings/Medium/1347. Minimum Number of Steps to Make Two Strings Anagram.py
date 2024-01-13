from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounter=Counter(s)
        tCounter=Counter(t)
        diff=sCounter-tCounter
        print(diff)
        return sum(diff.values())



sol=Solution()
s = "leetcode"
t = "practice"
print(sol.minSteps(s,t))
    



        