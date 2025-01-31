
import heapq
from typing import List
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        heap=[(0,0,0)] # (cost , x, y)
        visited=set()
        rows,col=len(grid),len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up


        while heap:
            cost,x,y=heapq.heappop(heap)

            if (x,y) in visited:
                continue

            visited.add((x,y))

            if (x,y) == (rows-1,col-1):
                return cost


            # change direction
            newDir=grid[x][y]-1
            newRow,newCol=directions[newDir]
            if 0<=x+newRow<rows and 0<=y+newCol<col:
                heapq.heappush(heap,(cost,x+newRow,y+newCol))

            for i in range(4):
                if i == newDir:
                    continue

                newRow,newCol=directions[i]

                if 0<=x+newRow<rows and 0<=y+newCol<col:
                    heapq.heappush(heap,(cost+1,x+newRow,y+newCol))

        return -1

s=Solution()
                



        
