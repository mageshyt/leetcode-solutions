class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache={}

        def dp(i,j):
            # base case
            if (i,j) in cache:
                return cache[(i,j)]
            
            # if both reach the end of the string then return True
            if i==len(s) and j==len(p):
                return True
            
            # if only pattern reaches the end of the string then return False
            elif j==len(p):
                return False
            
            # if only string reaches the end of the string then check if the remaining pattern is all *
            elif i==len(s):
                return p[j]=='*' and dp(i,j+1)
            
            # if the current character is * then we have two choices
            # 1. we can skip the current character in the pattern
            # 2. we can skip the current character in the string
            elif p[j]=='*':
                cache[(i,j)]=dp(i,j+1) or dp(i+1,j)

            # if the current character is ? or the current character in the string and pattern are same then we can skip both
            elif p[j]=='?' or p[j]==s[i]:
                cache[(i,j)]=dp(i+1,j+1)

            # if the current character in the string and pattern are not same then return False
            else:
                cache[(i,j)]=False

            return cache[(i,j)]
        
        return dp(0,0)
    
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
    
            
