"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        self.dfs(s, set(), 0)
        return self.ans

    def dfs(self, s, seen, idx):
        print(seen)
        if idx== len(s):
            self.ans=max(self.ans, len(seen))

        for i in range(idx, len(s)):
            # check if the substring is unique
            substr=s[idx:i+1]

            if substr in seen:
                continue

            seen.add(substr)
            self.dfs(s, seen, i+1)
            seen.remove(substr)

# Time complexity: O(2**N)
print(Solution().maxUniqueSplit("ababccc")) # 5
