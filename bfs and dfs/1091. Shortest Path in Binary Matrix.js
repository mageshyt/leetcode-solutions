`Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1`;

const shortestPathBinaryMatrix = (grid) => {
  if (grid.length === 0 || grid[0][0] == 1) {
    return -1;
  }
  const directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
  ];

  const rows = grid.length;
  const cols = grid[0].length;

  const queues = [];
  queues.push([1, 0, 0]);
  console.log(queues);
  while (queues.length > 0) {
    const [direction, row, col] = queues.shift();
    //! if we reach the end
    if (row === rows - 1 && col === cols - 1) return direction;
    for (let [nextRow, nextCol] of directions) {
      const newRow = row + nextRow;
      const newCol = col + nextCol;
      if (
        newRow >= 0 &&
        newRow < rows &&
        newCol >= 0 &&
        newCol < cols &&
        grid[newRow][newCol] === 0
      ) {
        queues.push([direction + 1, newRow, newCol]);
        grid[newRow][newCol] = 1;
      }
    }
  }
  return -1;
};

console.log(
  shortestPathBinaryMatrix([
    [0, 1],
    [1, 0],
  ])
);
