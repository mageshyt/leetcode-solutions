`You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.

 

Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.`;
const dirs = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

const uniquePathsIII = (grid) => {
  let start = [];
  let res = 0;
  let count_zero = 1;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        start = [i, j];
      } else if (grid[i][j] === 0) {
        count_zero++;
      }
    }
  }

  const rows = grid.length;
  const cols = grid[0].length;

  const dfs = (i, j, count) => {
    // return if obstacle and visited
    if (grid[i][j] === -1 || grid[i][j] === "#") return;

    // if end
    if (grid[i][j] === 2) {
      if (count === count_zero) res++;
      return;
    }

    // mark as visited
    grid[i][j] = "#";
    for (const [x, y] of dirs) {
      const newRow = x + i;
      const newCol = y + j;
      // return if out of bounds
      if (newRow < 0 || newRow >= rows || newCol < 0 || newCol >= cols)
        continue;
      dfs(newRow, newCol, count + 1);
    }
    // unmark as visited
    grid[i][j] = 0;
  };

  dfs(start[0], start[1], 0);
  return res;
};

const res = uniquePathsIII([
  [1, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 2, -1],
]);

console.log(res);
