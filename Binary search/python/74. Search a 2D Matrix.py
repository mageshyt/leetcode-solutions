'''You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0 # start of the matrix
        right = rows * cols - 1 # end of the matrix

        while left <= right:
            mid = (left + right) // 2

            mid_val = matrix[mid // cols][mid % cols]  # 2D to 1D 

            # if we find the target, return true
            if mid_val == target:
                return True
            elif target > mid_val:
                # if the target is greater than the middle value, search the right half
                left = mid + 1
            else:
                # if the target is less than the middle value, search the left half
                right = mid - 1

        return False

 


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(s.searchMatrix(matrix, target))
