`
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100`;

const directions = [
  [1, 0],
  [1, 1],
  [1, -1],
];

const minFallingPathSum = (matrix) => {
  const [rows, cols] = [matrix.length, matrix[0].length];
  const memo = new Map();
  const dfs = (row, col) => {
    if (col < 0 || col === cols) return Infinity;
    if (!row) return matrix[row][col];

    const key = `${row}-${col}`;

    if (!memo.has(key)) {
      let a = dfs(row - 1, col - 1),
        b = dfs(row - 1, col),
        c = dfs(row - 1, col + 1);
      memo.set(key, Math.min(a, b, c) + matrix[row][col]);
    }
    return memo.get(key);
  };

  let min = Infinity;
  for (let col = 0; col < cols; col++) {
    min = Math.min(min, dfs(rows - 1, col));
  }
  return min;
};

console.log(
  minFallingPathSum([
    [2, 1, 3],
    [6, 5, 4],
    [7, 8, 9],
  ])
);
