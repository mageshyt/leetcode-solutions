"""A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
 

Constraints:

1 <= s.length <= 105
s consists of only digits and does not contain leading zeros.
1 <= k <= 109
Accepted
35K
Submissions
"""


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        cache = {}

        def dp(i):

            if i in cache:
                return cache[i]

            if i == len(s):
                return 1

            if s[i] == '0':
                return 0
            num = 0
            ans = 0
            for j in range(i, len(s)):
                num = num*10 + int(s[j])

                if num > k:
                    break

                ans += dp(j+1)

            cache[i] = ans

            return cache[i]

        return dp(0) % (10**9 + 7)

    def numberofArrays2(self,s,k):
        n=len(s)
        dp=[0]*(n+1)

        dp[n]=1

        for i in range(n-1,-1,-1):
            if s[i]=='0':
                continue
            num=0
            for j in range(i,n):
                num=num*10+int(s[j])
                if num>k:
                    break
                dp[i]+=dp[j+1]

        return dp[0]%(10**9+7)
    

if __name__ == "__main__":
    s = "1000"
    k = 131483660
    print(Solution().numberOfArrays(s, k))
