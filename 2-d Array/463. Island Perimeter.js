`You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4`;

const islandPerimeter = (grid) => {
  let noOfIsland = 0;
  let neighbors = 0;
  const row = grid.length;
  const col = grid[0].length;
  for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
      if (grid[r][c] === 1) {
        noOfIsland++;
        if (r < row - 1 && grid[r + 1][c] === 1) {
          neighbors++; //! count the next down neighbor
        }
        if (c < col && grid[r][c + 1] === 1) {
          neighbors++; //! count the next up neighbor
        }
      }
    }
  }
  //! if we get any up or down neighbor, we will have 2 perimeter
  return 4 * noOfIsland - 2 * neighbors;
};

console.log(
  islandPerimeter([
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
  ])
);

console.log(islandPerimeter([[1, 1]]));
