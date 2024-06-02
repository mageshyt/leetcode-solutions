
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left,right=0,len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

# Time complexity: O(n)
# Space complexity: O(1)
print(Solution().reverseString(["h","e","l","l","o"])) # ["o","l","l","e","h"]
