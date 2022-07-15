`You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 `;
const directions = [
  [1, 0], // Right
  [-1, 0], // Left
  [0, 1], // up
  [0, -1], // down
];
const maxAreaOfIsland = (grid) => {
  const row_len = grid.length;
  const col_len = grid[0].length;
  let max_area = 0;

  const visited = new Map();
  const dfs = (row, col) => {
    const key = `${row}-${col}`;
    if (
      row < 0 ||
      row >= row_len ||
      col < 0 ||
      col >= col_len ||
      grid[row][col] === 0 ||
      visited.get(key)
    ) {
      return 0;
    }
    visited.set(key, true);
    return (
      1 +
      dfs(row + 1, col) +
      dfs(row - 1, col) +
      dfs(row, col + 1) +
      dfs(row, col - 1)
    );
  };
  for (let row = 0; row < row_len; row++) {
    for (let col = 0; col < col_len; col++) {
      const key = `${row}-${col}`;
      if (grid[row][col] === 1 && !visited.has(key)) {
        max_area = Math.max(max_area, dfs(row, col));
      }
    }
  }
  return max_area;
};

const grid = [
  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
];

console.log(maxAreaOfIsland(grid));

const solution = (grid) => {
  const rows = grid.length;
  const cols = grid[0].length;

  const visited = new Map();

  const dfs = (row, col, area = 1) => {
    const key = `${row}-${col}`;
    if (visited.has(key)) return 0;
    visited.set(key, true);

    if (
      row >= rows ||
      row < 0 ||
      col >= cols ||
      col < 0 ||
      grid[row][col] === 0
    )
      return 0;
    for (let [x, y] of directions) {
      const newRow = row + x;
      const newCol = col + y;
      area += dfs(newRow, newCol);
    }
    return area;
  };

  let max_area = 0;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === 1) {
        const area = dfs(r, c);
        max_area = Math.max(max_area, area);
      }
    }
  }
  return max_area;
};

console.log(solution(grid));
