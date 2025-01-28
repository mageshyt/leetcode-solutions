

from typing import List
from collections import deque
class Solution:
    def highestPeak(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols=len(mat),len(mat[0])
        res=[[-1]*cols for _ in range(rows)]


        q=deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col]==1:
                    q.append((row,col))
                    res[row][col]=0

        while q:
            row,col=q.popleft()
            for r,c in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_row,new_col=row+r,col+c
                if 0<=new_row<rows and 0<=new_col<cols and res[new_row][new_col]==-1:
                    res[new_row][new_col]=res[row][col]+1
                    q.append((new_row,new_col))

        return res

