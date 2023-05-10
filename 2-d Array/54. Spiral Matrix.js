`Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
`;

const spiralOrder = (matrix) => {
  `
    1.Right
    2.Down
    3.Left
    4.Up
    `;

  const rows = matrix.length;
  const cols = matrix[0].length;

  const res = [];

  let top = 0;
  let bottom = rows - 1;

  let left = 0;
  let right = cols - 1;

  while (top <= bottom && left <= right) {
    // first put left

    for (let col = left; col <= right; col++) {
      res.push(matrix[top][col]);
    }
    top++;

    // then put down
    for (let row = top; row <= bottom; row++) {
      res.push(matrix[row][right]);
    }

    right--;

    // then put right

    if (top <= bottom) {
      for (let col = right; col >= left; col--) {
        res.push(matrix[bottom][col]);
      }
      bottom--;
    }

    // then put up
    if (left <= right) {
      for (let row = bottom; row >= top; row--) {
        res.push(matrix[row][left]);
      }
      left++;
    }
  }

  return res;
};

console.log(
  spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ])
);
