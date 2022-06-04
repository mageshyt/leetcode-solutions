`Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
`;

const longestIncreasingPath = (matrix) => {
  if (matrix.length === 0) return 0;

  const rows = matrix.length;

  const cols = matrix[0].length;

  const visited = new Map();

  const dfs = (r, c, prev) => {
    const key = `${r}-${c}`;
    if (c < 0 || c === cols || r < 0 || r === rows || prev >= matrix[r][c])
      return 0;
    if (visited.has(key)) return visited.get(key);

    const result =
      1 +
      Math.max(
        dfs(r + 1, c, matrix[r][c]),
        dfs(r - 1, c, matrix[r][c]),
        dfs(r, c + 1, matrix[r][c]),
        dfs(r, c - 1, matrix[r][c])
      );
    visited.set(key, result);
    return result;
  };

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      dfs(row, col, -1);
    }
  }
  return Math.max(...visited.values());
};

console.log(
  longestIncreasingPath([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
  ])
);
