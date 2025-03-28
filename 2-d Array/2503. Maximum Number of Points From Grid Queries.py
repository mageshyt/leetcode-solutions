"""
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.
"""

from typing import List
import heapq
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions=[(0,1),(0,-1),(1,0),(-1,0)] # up,down,left,right
        rows,cols=len(grid),len(grid[0])

        res=[0] * len(queries)

        # sort the queries
        q=[ (num,idx) for idx,num in enumerate(queries)]
        q.sort() # sort based on num

        heap=[(grid[0][0],0,0)] # (val,row,count)

        points=0
        visited=set()
        visited.add((0,0))

        for limit,idx in q:
            while heap and heap[0][0] < limit:
                val,r,c=heapq.heappop(heap)
                points+=1
                neighbors=[(r+dx,c+dy) for dx,dy in directions if 0<=r+dx<rows and 0<=c+dy<cols]

                for nr,nc in neighbors:
                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        heapq.heappush(heap,(grid[nr][nc],nr,nc))
            res[idx]=points

        return res

grid = [[1,2,3],[2,5,7],[3,5,1]]
queries = [5,6,2]
print(Solution().maxPoints(grid,queries)) #[3,2,2]
