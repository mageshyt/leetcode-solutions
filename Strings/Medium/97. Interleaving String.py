"""Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 """


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        cache={}
        def dfs(a=0,b=0,c=0):
            # base case
            if c==len(s3):
                return a==len(s1) and b==len(s2)
            
            if (a,b,c) in cache:
                return cache[(a,b,c)]
            
            ans=False
            if a<len(s1) and s1[a]==s3[c]:
                ans|=dfs(a+1,b,c+1)

            if b<len(s2) and s2[b]==s3[c]:

                ans|=dfs(a,b+1,c+1)


            cache[(a,b,c)]=ans

            return ans
        
        return dfs(0,0,0)

    

s1 = "a"
s2 = "b"


print(Solution().isInterleave(s1,s2,"d"))
    



