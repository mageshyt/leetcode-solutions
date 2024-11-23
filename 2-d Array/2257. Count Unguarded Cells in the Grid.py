"""
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.
"""

from typing import List
from collections import deque
class Solution:

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        # 0 = free , 1= guard, 2= wall , 3 =  guarded

        for r,c in guards:
            grid[r][c]=1


        for r,c in walls:
            grid[r][c]=2

        
        def mark_guarded(r,c):
            # horizontally
            for row in range(r+1,m):

                # if we have any wall or guard, break
                if grid[row][c] == 2 or grid[row][c] == 1:
                    break



                grid[row][c] = 3

            for row in range(r-1,-1,-1):
                if grid[row][c] == 2 or grid[row][c] == 1:
                    break
                grid[row][c] = 3

            # vertically
            for col in range(c+1,n):
                if grid[r][col] == 2 or grid[r][col] == 1:
                    break
                grid[r][col] = 3

            for col in range(c-1,-1,-1):
                if grid[r][col] == 2 or grid[r][col] == 1:
                    break
                grid[r][col] = 3



        for r,c in guards:
            mark_guarded(r,c)

        return sum(row.count(0) for row in grid)




if __name__ == "__main__":
    s = Solution()
    m = 4
    n = 6
    guards =[[0,0],[1,1],[2,3]]
    walls =[[0,1],[2,2],[1,4]]
    print(s.countUnguarded(m, n, guards, walls))


