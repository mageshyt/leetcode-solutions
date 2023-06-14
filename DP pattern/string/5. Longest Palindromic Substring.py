class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = 0
        res_str = ''

        for i in range(len(s)):
            # for odd length
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > res:
                    res = right-left+1
                    res_str = s[left:right+1]
                left -= 1
                right += 1

            # for even length
            left = i
            right = i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > res:
                    res = right-left+1
                    res_str = s[left:right+1] # update the res_str
                left -= 1
                right += 1

        return res_str
