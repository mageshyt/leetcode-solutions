"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
"""
from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        row_min = [min(row) for row in matrix]
        col_max = [max([matrix[i][j] for i in range(rows)]) for j in range(cols)]

        res=[]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==row_min[i]==col_max[j]:
                    res.append(matrix[i][j])

        return res

print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])) # [15]
print(Solution().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])) # [12]
print(Solution().luckyNumbers([[7,8],[1,2]])) # [7]
