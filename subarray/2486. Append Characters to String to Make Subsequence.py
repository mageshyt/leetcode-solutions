"""
You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.



Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
Example 2:

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").
Example 3:

Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left,right=0,0

        while left<len(s) and right<len(t):
            if s[left]==t[right]:
                left,right=left+1,right+1
            else:
                left+=1

        return len(t)-right# return the number of characters that need to be appended to the end of s

# Time complexity: O(n)
# Space complexity: O(1)
print(Solution().appendCharacters("coaching","coding")) # 4
print(Solution().appendCharacters("12ssa","a")) # 0
print(Solution().appendCharacters("z","abcde")) # 5
