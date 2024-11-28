

import heapq
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        heap=[(0,0,0)] # distance, row, col
        rows, cols=len(grid), len(grid[0])

        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=set()

        while heap:
            distance, row, col=heapq.heappop(heap)

            if row == rows-1 and col == cols-1:
                return distance

            if (row, col) in visited:
                continue

            visited.add((row, col))
            for dr, dc in directions:
                new_row, new_col=row+dr, col+dc

                if 0<=new_row<rows and 0<=new_col<cols:
                    new_distance=distance+grid[new_row][new_col]
                    heapq.heappush(heap, (new_distance, new_row, new_col))
        return -1


grid = [[0,1,1],[1,1,0],[1,1,0]]
print(Solution().minimumObstacles(grid)) # 1




            

