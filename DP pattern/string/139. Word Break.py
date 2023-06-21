class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # make a hash map to store the words
        words = {}
        for word in wordDict:
            words[word] = 1
        print(words)
        dp = {}

        def helper(i: int, words):
            # base case
            print(dp)
            if i == len(s):
                return True

            if i in dp:
                return dp[i]

            dp[i] = False
            # recursive case

            for j in range(i+1, len(s)+1):
                if s[i:j] in words and helper(j, words):
                    dp[i] = True

            return dp[i]
        return helper(0, words)


s = "leetcode"

wordDict = ["leet", "code"]

print(Solution().wordBreak(s, wordDict))
