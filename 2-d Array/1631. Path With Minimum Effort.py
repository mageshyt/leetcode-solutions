


'''You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.'''



from collections import deque


class Solution:
    def minimumEffortPath(self, heights):
        row, col = len(heights), len(heights[0])
        left=0
        right=pow(10,6)
        if row==1 and col==1:
            return 0
        direction=[(0,1),(0,-1),(1,0),(-1,0)]

        def connect(target):
            visited=set()
            queue=deque()
            def enqueue(x,y):
                queue.append((x,y))
                visited.add((x,y))
            enqueue(0,0)
            # search in all directions
            while len(queue)>0:
                x,y=queue.popleft()
                for dx,dy in direction:
                    newRow=x+dx
                    newCol=y+dy
                    if 0<=newRow< row and 0<=newCol<col and (newRow,newCol) not in visited and\
                          abs(heights[newRow][newCol] - heights[x][y]) <= target:
                        enqueue(newRow,newCol)
                        if newRow==row -1 and newCol==col -1:
                            return True
            return False

        # both left and right are possible ans
        while left<right:
            mid=(left+right)//2 # get out mid
            if connect(mid):
                # mid would be our ans
                right=mid
            else:
                left=mid+1
        return left
if __name__ == '__main__':
    num =[[1,10,6,7,9,10,4,9]]
    print(Solution().minimumEffortPath(num))