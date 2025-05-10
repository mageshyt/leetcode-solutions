"""
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.
Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 3


"""


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        heap=[(0,0,0)] # (time,row,col)
        visited=set()
        rows,cols=len(moveTime),len(moveTime[0])

        while heap:
            time,row,col=heapq.heappop(heap)

            if(row,col) ==(rows-1,cols-1):
                return time

            if(row,col) in visited:
                continue

            visited.add((row,col))

            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                newX,newY=dx+row,dy+col

                if 0<=newX<rows and 0<=newY<cols:
                    nextTime=max(moveTime[newX][newY]+1,time+1)
                    heapq.heappush(heap,(nextTime,newX,newY))
        return -1
