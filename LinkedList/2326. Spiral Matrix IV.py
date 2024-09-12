"""
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.


"""

class Solution:
    def spiralmatrix(self,m:int,n:int,head):
        
        matrix=[[-1]*n for _ in range(m)] # create a matrix with -1

        # fill the matrix with the linked list values
        current=head

        directions=[(0,1),(1,0),(0,-1),(-1,0)] # right, down, left, up
        row, col=0,0
        direction=0

        while current:
            # fill the matrix with the linked list values
            matrix[row][col]=current.val

            # check if the next cell is out of bounds or already filled
            dy, dx=directions[direction]

            if row+dy < 0 or row+dy >= m or col+dx < 0 or col+dx >= n or matrix[row+dy][col+dx]!=-1:
                direction=(direction+1)%4
                dy, dx=directions[direction]

            row+=dy
            col+=dx
            current=current.next

        return matrix
