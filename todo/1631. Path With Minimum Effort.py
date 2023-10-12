from collections import deque
import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        minHeap=[[0,0,0]] # [effort, row, col]
        visited=set()

        while minHeap:
            effort, row, col=heapq.heappop(minHeap)

            if (row,col) in visited:
                continue

            visited.add((row,col))

            if (row,col)==(rows-1,cols-1):
                    return effort
            
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                newRow=row+dx
                newCol=col+dy

                # boundary check

                if 0<=newRow<rows and 0<=newCol<cols and (newRow,newCol) not in visited:
                    # calculate new effort 
                    newEffort=abs(heights[newRow][newCol]-heights[row][col])
                    # push to minHeap
                    heapq.heappush(minHeap,[max(effort,newEffort),newRow,newCol])

        return -1