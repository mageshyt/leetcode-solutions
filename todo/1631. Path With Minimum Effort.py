from collections import deque


class Solution:
    def minimumEffortPath(self, heights):
        row, col = len(heights), len(heights[0])
        left=0
        right=pow(10,6)
        if row ==1 and col ==1:
            return 0
        direction=[(0,1),(0,-1),(1,0),(-1,0)]

        def connect(target):
            visited=[[False] * col for _ in range(row)]
            queue=deque()
            def enqueue(x,y):
                queue.append((x,y))
                visited[x][y]=True
            enqueue(0,0)
            # search in all directions
            while (queue):
                x,y=queue.popleft()
                for dx,dy in direction:
                    newRow=x+dx
                    newCol=y+dy
                    if 0<=newRow< row and 0<=newCol<col and not visited[newRow][newCol] and\
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