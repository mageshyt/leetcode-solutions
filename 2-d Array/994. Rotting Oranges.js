`You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

`;

const orangesRotting = (grid) => {
  //! we are going to use bfs
  const queue = [];
  const rows = grid.length;
  const cols = grid[0].length;
  let fresh = 0;
  let time = 0;
  // !directions
  const directions = [
    [0, 1], // up
    [0, -1], // down
    [1, 0], // Right
    [-1, 0], // Left
  ];

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === 2) {
        queue.push([r, c]);
      }
      if (grid[r][c] === 1) {
        fresh++;
      }
    }
  }

  while (queue.length > 0 && fresh > 0) {
    for (let i = 0; i < queue.length; i++) {
      const [r, c] = queue.shift();
      for (let [dr, dc] of directions) {
        const newRow = r + dr;
        const newCol = c + dc;
        if (
          newRow < 0 ||
          newRow == rows ||
          newCol < 0 ||
          newCol == cols ||
          grid[newRow][newCol] !== 1
        )
          continue;
        grid[newRow][newCol] = 2;
        queue.push([newRow, newCol]);
        fresh--;
      }
    }
    time++;
  }
  return fresh === 0 ? time : -1;
};

console.log(
  orangesRotting([
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
  ])
);
console.log(
  orangesRotting([
    [2, 1, 1],
    [1, 1, 1],
    [0, 1, 2],
  ])
);
