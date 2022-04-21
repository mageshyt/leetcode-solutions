`Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3`;

const numIslands = (grid) => {
  let count = 0;
  let rows = grid.length;
  let cols = grid[0].length;
  const visited = new Map();
  // direction array
  const directions = [
    [1, 0], // Right
    [-1, 0], // Left
    [0, 1], // up
    [0, -1], // down
  ];
  const bfs = (row, col) => {
    const queue = [[row, col]];
    const key = `${row}-${col}`;
    visited.set(key, true);
    while (queue.length) {
      const [r, c] = queue.pop();
      for (let [dr, dc] of directions) {
        const newRow = dr + r;
        const newCol = dc + c;
        if (
          newRow >= 0 &&
          newRow < rows &&
          newCol >= 0 &&
          newCol < cols &&
          grid[newRow][newCol] === "1" &&
          !visited.get(`${newRow}-${newCol}`)
        ) {
          queue.push([newRow, newCol]);
          visited.set(`${newRow}-${newCol}`, true);
        }
      }
    }
  };

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const key = `${r}-${c}`;
      if (grid[r][c] === "1" && !visited.has(key)) {
        dfs(r, c);
        count++;
      }
    }
  }
  return count;
};

console.log(
  numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
  ])
);
