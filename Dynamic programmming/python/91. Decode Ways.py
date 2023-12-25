class Solution:
    def numDecodings(self, s: str) -> int:
        cache={}

        def dp(i):
            # base case
            # 1. if already calculated

            if  i in cache:
                return cache[i]
            # 2. if reach the end of string
            if i == len(s):
                return 1
            
            # 3. if current character is 0
            if s[i] == '0':
                return 0
            
            if i == len(s)-1:
                return 1

            # 4. if current character is 1 or 2 and next character is less than 7
            # one move 
            ans = dp(i+1) 
            # two move if next char is < 7 when current is 2
            if s[i] == '1' or (s[i] == '2' and s[i+1] < '7'):
                ans += dp(i+2)
            cache[i] = ans
            return ans
        return dp(0)

if __name__ == '__main__':
    print(Solution().numDecodings('10'))