'''There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
      dp=[[0]*n for _ in range(m)]
      dp[startRow][startColumn]=1 # mark the start position

      direction=[(1,0),(-1,0),(0,1),(0,-1)]

      ans=0     
      mod=10**9+7
      for _ in range(maxMove):
        new_table=[[0]*n for _ in range(m)]
        for r in range(m):
          for c in range(n):

            for [row,col] in direction:
              new_r=r+row
              new_c=c+col
              if new_r<0 or new_r>=m or new_c<0 or new_c>=n:
                ans+=dp[r][c] # if out of boundary, add the number of paths from the old position
              else:
                new_table[new_r][new_c]+=dp[r][c] # if inbound, add the number of paths from the old position
                new_table[new_r][new_c]%=mod

        dp=new_table
      return  ans%mod

if __name__ == '__main__':
  s=Solution()
  print(s.findPaths(2,2,2,0,0))
