"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word"""

from collections import Counter

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        cache = {}  # Dictionary to store results of subproblems
        words = Counter(wordDict)  # Count occurrences of each word in the wordDict

        def dfs(i):
            # Base case: If we have reached the end of the string, return True
            if i == len(s):
                return True

            if i in cache:
                return cache[i]  # Return the result from cache if available

            cache[i] = False  # Initialize the cache for current index

            # Try all possible substrings starting from the current index
            for endStr in range(i + 1, len(s) + 1):
                new_word = s[i:endStr]  # Extract the substring from current index to endStr

                # If the new_word is in the wordDict and the rest of the string can be broken
                # recursively, update the cache and return True
                if new_word in words and dfs(endStr):
                    cache[i] = True
                    break  # Break the loop since we found a valid word

            return cache[i]

        return dfs(0)  # Start the recursive function call from the beginning of the string

    








s="leetcode"
words=["leet","code"]
print(Solution().wordBreak(s,words))