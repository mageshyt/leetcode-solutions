import re


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows=len(matrix)
        cols=len(matrix[0])

        dp={}
        def dfs(r,c,pre):
            if r<0 or r==rows or c<0 or c ==cols or matrix: return 0

            res=1+max(
                dfs(r-1,c,pre),
                dfs(r+1,c,pre),
                dfs(r,c-1,pre),
                dfs(r,c+1,pre)
            )
            if (r,c) not in dp:
                dp[(r,c)]=res
        
        for row in range(rows):
            for col in range(cols):
                dfs(row,col,matrix[row][col])
        print (dp)
        return max(dp.values())

        
if __name__ == '__main__':
    matrix=[[9,9,4],[6,6,8],[2,1,1]]
    print (Solution().longestIncreasingPath(matrix))