from ast import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        dp={}
        def dfs(l,r):

            if (l,r) in dp:
                return dp[(l,r)]
            
            if r-l<=1:
                return 0
            
            ans=float('inf')

            for cut in cuts:
                if l<cut<r:
                    ans=min(ans,dfs(l,cut)+(r-l)+dfs(cut,r))

            dp[(l,r)]=ans =0 if ans==float('inf') else ans
            return dp[(l,r)]
        

        return dfs(0,n)
