'''`A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
Example 2:

Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
 `;

const diagonalSort = (mat) => {
};

console.log(
  diagonalSort([
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2],
  ])
);'''
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat )  :

      rows, cols = len(mat), len(mat[0]) # rows, cols 
      temp=defaultdict(list) # temp is a dictionary with key as the diagonal number and value as a list of elements in that diagonal
      for i in range(rows):
          for j in range(cols):
              temp[i-j].append(mat[i][j])

      # sort the numbers in each row in reverse order
      for nums in temp.values():
          nums.sort( reverse=True)  

      for i in range(rows):
          for j in range(cols):
              mat[i][j] = temp[i-j].pop()

      return mat

s = Solution()
print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))