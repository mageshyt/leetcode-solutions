`An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

 

Example 1:


Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
Example 2:


Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.`;

const checkValid = (grid) => {
  const rows = grid.length;
  const cols = grid[0].length;

  const visited_rows = new Array(rows).fill(0).map(() => new Set());
  const visited_cols = new Array(cols).fill(0).map(() => new Set());

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const num = grid[i][j];

      if (visited_rows[i].has(num) || visited_cols[j].has(num)) {
        return false;
      }
      visited_rows[i].add(num);
      visited_cols[j].add(num);
    }
  }

  return true;
};
