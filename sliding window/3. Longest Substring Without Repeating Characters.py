'''Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        windowStart = 0
        maxLength = 0

        seen = {}

        windowEnd = 0

        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]  # current char
            if rightChar in seen:
                # if already in seen, move windowStart to the right of the last seen char
                # move to next place
                windowStart = max(windowStart, seen[rightChar] + 1)

            seen[rightChar] = windowEnd  # set the char
            # to get max len we have to do end - start +1
            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
