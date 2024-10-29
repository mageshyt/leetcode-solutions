"""
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.


"""
from typing import List
from collections import deque 
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited=set()
        q=deque()

        for i in range(rows):
            visited.add((i,0))
            q.append((i,0,0)) # row, col, moves


        max_moves=0

        def is_valid(row,col):
            return 0<=row<rows and 0<= col<cols and (row,col) not in visited 


        def getNeighbours(row,col):
            dir=[(0,1),(1,1),(-1,1)]

            for r,c in dir:
                new_row,new_col=row+r,col+c

                if is_valid(new_row,new_col) and grid[new_row][new_col]>grid[row][col]:
                    yield new_row,new_col

        while q:
            row,col,moves = q.popleft()
            max_moves=max(max_moves,moves)

            for new_row,new_col in getNeighbours(row,col):
                visited.add((new_row,new_col))
                q.append((new_row,new_col,moves+1))

        return max_moves

    # dp solution
    def maxMovesDp(self,grid:List[List[int]])->int:
        rows,cols=len(grid),len(grid[0])
        dp={}

        def dfs(row,col)->int:
            if (row,col) in dp:
                return dp[(row,col)]

            max_moves=0

            for r,c in [(0,1),(1,1),(-1,1)]: # right, down, up
                new_row,new_col=row+r,col+c

                if 0<=new_row<rows and 0<=new_col<cols and \
                     grid[new_row][new_col]>grid[row][col]:
                    max_moves=max(max_moves,dfs(new_row,new_col)+1)

            dp[(row,col)]=max_moves

            return max_moves

        res=0

        for i in range(rows):
            res=max(res,dfs(i,0))

        return res






print(Solution().maxMoves([[3,2,4],[2,1,9],[1,1,7]])) #3
