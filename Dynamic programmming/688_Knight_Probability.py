
from typing import List
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp={}

        directions=[
                   (1,2) , # top right
                   (-1,2), # top left
                   (2,1) , # left top
                   (2,-1), # left down
                   (-2,1), # right top
                   (-2,-1),# right down
                   (1,-2), # bottom right
                   (-1,-2), # bottom left
                       ]

        def dfs(r,c,k):
               # out of bound case
                if r>=n or r<0 or c >= n or c < 0 :
                   return 0
               # when no moves the probility is 1
                if k==0:
                   return 1

                if (r,c,k) in dp:
                   return dp[(r,c,k)]
  

                res=0

                for dir in directions:
                    row,col=dir
                    newR=r+row
                    newC=c+col
                    res+=dfs(newR,newC,k-1)/8

                dp[(r,c,k)]=res

                return res;
        return dfs(row,column,k)
    



if __name__ == "__main__":

     print(Solution().knightProbability(3,2,0,0))





