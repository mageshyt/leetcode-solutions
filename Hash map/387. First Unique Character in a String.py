
from collections import deque
from collections import Counter
class Solution:
    # Time O(n) | Space O(n)
    def firstUniqChar(self, s: str) -> int:
        seen=Counter(s)
        for i in range(len(s)):
            if seen[s[i]]==1:
                return i
            
        return -1
    def firstUniqChar2(self, s: str) -> int:
        left=s[0]
        seen=set()

        for right in range(1,len(s)):
            if left==s[right]:
                seen.add(left)
                left=s[right]
                continue
            if left in seen:
                left=s[right]
                continue

        return -1
    


        # create a dictionary of the characters in s


print(Solution().firstUniqChar2("leetcode")) # 0