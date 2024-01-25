class Solution:
    # Time O(n*m) | Space O(n*m)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache={}
        n=len(text1)
        m=len(text2)
        def lcs(i,j):
            if i==n or j==m:
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            # 1. if the characters match then move both the pointers
            if text1[i]==text2[j]:
                cache[(i,j)]=1+lcs(i+1,j+1)
            
            # 2. if the characters do not match then move either of the pointers
            else:
                cache[(i,j)]=max(lcs(i+1,j),lcs(i,j+1))

            return cache[(i,j)]
        
        return lcs(0,0)
    
    # Top down approach
    # Time O(n*m) | Space O(n*m)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n=len(text1)
        m=len(text2)
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                # 1. if the characters match then move both the pointers
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                
                # 2. if the characters do not match then move either of the pointers
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return dp[n][m]

    
# Time complexity: O(n*m)
# Space complexity: O(n*m)
    
print(Solution().longestCommonSubsequence("abcde","ace")) # 3
