
"""Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter_s=Counter(s)

        



if __name__ == "__main__":
    obj = Solution()
    print(obj.removeDuplicateLetters("bcabc"))
