`Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false`;

const searchMatrix = (matrix, target) => {
  let row = 0;
  let col = matrix[0].length - 1;

  while (row < matrix.length && col >= 0) {
    if (matrix[row][col] === target) return true;
    if (matrix[row][col] > target) {
      col--;
    } else {
      row++;
    }
  }
  return false;
};
console.log(
  searchMatrix(
    [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 60],
    ],
    3
  )
);

//  Binary search solution

const searchMatrix2 = (matrix, target) => {
  // get the rows and cols
  const rows = matrix.length;
  const cols = matrix[0].length;

  // left and right pointers for binary search
  let left = 0;
  let right = rows * cols - 1;

  while (left <= right) {
    // get the mid idx using Math.floor
    let mid = Math.floor((left + right) / 2);

    // get the midIdx element  Math.floor(mid/cols) => row, mid%cols => col
    const midElement = matrix[Math.floor(mid / cols)][mid % cols];

    if (midElement === target) {
      // if midElement === target, then return true
      return true;
    }

    if (midElement < target) {
      // if midElement < target, then we will search the right part of the matrix
      left = mid + 1;
    } else {
      // if midElement > target, then we will search the left part of the matrix
      right = mid - 1;
    }
  }

  return false;
};
