"""Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]"""
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()

        # Initialize the queue with 0 cells and mark other cells as infinity
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        # Perform BFS traversal starting from 0 cells
        while queue:
            row, col = queue.popleft()
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                # Check if the new position is out of bounds
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue

                # If the current distance is less than the newly calculated distance,
                # no need to update the cell or enqueue it
                if mat[new_row][new_col] <= mat[row][col] + 1:
                    continue

                # Update the cell with the new distance and enqueue it
                queue.append((new_row, new_col))
                mat[new_row][new_col] = mat[row][col] + 1

        return mat


mat = [[0,0,0],[0,1,0],[1,1,1]]

print(Solution().updateMatrix(mat))
