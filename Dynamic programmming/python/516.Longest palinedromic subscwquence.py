

class Solution:
    def longestPalindromeSubseq(self, str: string) -> int:
        length = 1
        cache = {}

        def dfs(left, right):
            # out of range
            if left < 0 or right == len(str):

                return 0
            elif (left, right) in cache:
                return cache[(left, right)]
            if str[left] == str[right]:
                length = 1 if left == right else 2
                cache[(left, right)] = length + dfs(left-1, right+1)

            else:
                # 1 move left pointer
                # 2 move right pointer
                cache[(left, right)] = max(
                    dfs(left-1, right), dfs(left, right+1))

            return cache[(left, right)]

        for i in range(len(str)):
            dfs(i, i)  # odd length
            dfs(i, i+1)  # even length

        return max(cache.values())
    
    def solution2(self,str):
        dp=[[0]*(len(str)+1) for _ in range(len(str)+1)]

        res=0

        for i in range(len(str)):
            for j in  range(len(str)-1,i-1,-1):

                if str[i]==str[j]:
                    dp[i][j]=1 if i==j else 2

                    if i -1 >=0:
                        dp[i][j]+=dp[i-1][j+1]


                else:
                    dp[i][j]=dp[i][j+1]

                    if i-1 >=0:

                        dp[i][j]=max(dp[i][j],dp[i-1][j])

                res=max(res,dp[i][j])


        return res
    


