'''Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]'''

class Solution:
    def spiralOrder(self, matrix ):

        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        result = []

        top = 0 # top row
        bottom = rows - 1 # bottom row

        left = 0 # left column

        right = cols - 1 # right column

        while top <= bottom and left <= right:
            # top row
            for i in range(left,right + 1):
                result.append(matrix[top][i]) # append top row

            top += 1 # increment top row by 1 to move to next row (down) 👇🏻

            # right column
            for i in range(top,bottom+1):
                result.append(matrix[i][right]) # append right column 

            right -= 1 # decrement right column by 1 to move to next column (left) 👈🏻

            # bottom row
            for i in reversed(range(left,right+1)):
                if top <= bottom:
                    result.append(matrix[bottom][i])

            bottom -= 1 # decrement bottom row by 1 to move to next row (up) 👆🏻

            # left column

            for i in reversed(range(top,bottom+1)):
                if left <= right:
                    result.append(matrix[i][left])

            left += 1 # increment left column by 1 to move to next column (right) 👉🏻

     
        return result
 

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().spiralOrder(matrix))
