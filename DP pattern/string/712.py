"""case 1 : some ith and jth character matches in both string
case 2 : it doesn't matches

so we have two casses , lets us analyze them one by one 
case 1 : if some ith and jth character matches then we can reduce the ASCII sum if we include both ith and jth character in sequence, s
o we dont add their's ASCII values 
case 2 : ith and jth character doesn't matches , so we have 2 option for these
	option 1 : skip ith character assuming jth character might be useful later on , so we add ASCII of ith and recurr for rest 
	option 2 : skip jth character assuming ith matches somewhere late in string , same as option 1 for other string"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        cols=len(s2)
        rows=len(s1)
        dp=[[0]* (cols+1) for _ in range(rows+1)]


        for i in range(rows):
            for j in range(cols):
                if s1[i]==s2[j]:
                    dp[i+1][j+1]=dp[i][j] + ord(s1[i])
                else:
                    dp[i+1][j+1]=max(dp[i][j+1] ,dp[i+1][j ])

        result = sum(map(ord, s1 + s2)) - dp[rows][cols] * 2
       
        print(sum(map(ord, s1 + s2)))
        return result
    
    def solution2(self,s1,s2):
        dp={}

        def dfs(i,j):

            if i == len(s1) and j == len(s2):
                return 0
            
            if i == len(s1):
                return sum(map(ord,s2[j:]))
            
            if j == len(s2):
                return sum(map(ord,s1[i:]))
            

            if (i,j) in dp:
                return dp[(i,j)]
            
            ans=0
            if s1[i] == s2[j]:
                # move on
                ans=dfs(i+1,j+1)

            else:
                # 1 we can delete ith character
                # 2 we can delete jth character
                ans=min(
                    dfs(i+1,j)+ord(s1[i]),
                    dfs(i,j+1)+ord(s2[j])
                ) 

            dp[(i,j)]=ans

            return dp[(i,j)]

        return dfs(0,0)
    

    

print(Solution().solution2("sea","eat"))
print(Solution().minimumDeleteSum("sea","eat"))

 