"""Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false"""

class Solution:

    
    def searchMatrix(self, matrix , target: int) -> bool:
        row=0
        col=len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target: return True
            if matrix[row][col] > target:
                col-=1
            else:
                row+=1

        return  False
       





if __name__ == '__main__':
    s=Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))