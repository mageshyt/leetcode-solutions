class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # make a hash map to store the words
        words = {}
        for word in wordDict:
            words[word] = 1

        dp={}
        def helper(i: int, words):

            # base case
            if i == len(s):
                return True

            if i in dp:
                return dp[i]
            
            dp[i] = False
            # recursive case

            for j in range(i+1, len(s)+1):
                if s[i:j] in words and helper(j, words):
                    dp[i] = True
                    return True
                
            return False
        return helper(0, words)


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"

wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
            "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

print(Solution().wordBreak(s, wordDict))
