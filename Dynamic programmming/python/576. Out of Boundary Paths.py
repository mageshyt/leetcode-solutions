
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache={}
        MOD=10**9+7
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j,move):
            if move<0:
                return 0
            # when we are out of bounds
            if i<0 or i>=m or j<0 or j>=n:
                return 1
            
            if (i,j,move) in cache:
                return cache[(i,j,move)]
            
            count=0
            for x,y in directions:
                count+=dfs(i+x,j+y,move-1)

            cache[(i,j,move)]=count%MOD
            return cache[(i,j,move)]
        
        return dfs(startRow,startColumn,maxMove)