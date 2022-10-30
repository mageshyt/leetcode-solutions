`You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0`;

const shortestPath = (grid, k) => {
  const rows = grid.length;
  const cols = grid[0].length;
  const directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  const queue = [[0, 0, 0, k]];
  const visited = new Set();

  while (queue.length > 0) {
    let [x, y, steps, obstacles] = queue.shift();
    const key = `${x}-${y}-${obstacles}`;
    // if the key is already visited, skip or step is less than 0
    if (visited.has(key) || obstacles < 0) continue;

    // if we reach the end, return the steps
    if (x === rows - 1 && y === cols - 1) return steps;

    // mark the key as visited
    visited.add(key);
    // ! if the current cell is an obstacle, increment the obstacles
    if (grid[x][y] === 1) obstacles--;

    // go to all directions
    for (const [dx, dy] of directions) {
      const newRow = x + dx;
      const newCol = y + dy;
      // if the new row and col is valid, push to the queue
      // if row is less than 0 or greater than rows or col is less than 0 or greater than cols then skip
      if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
        queue.push([newRow, newCol, steps + 1, obstacles]);
      }
    }
  }
  return -1;
};

console.log(
  shortestPath(
    [
      [0, 0, 0],
      [1, 1, 0],
      [0, 0, 0],
      [0, 1, 1],
      [0, 0, 0],
    ],
    1
  )
);

console.log(
  shortestPath(
    [
      [0, 1, 1],
      [1, 1, 1],
      [1, 0, 0],
    ],
    1
  )
);
