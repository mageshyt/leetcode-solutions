`There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
`;

const pacificAtlantic = (heights) => {
  const rows = heights.length;
  const cols = heights[0].length;

  // direction: [row, col]
  const directions = [
    [-1, 0],
    [0, -1],
    [0, 1],
    [1, 0],
  ];

  const dfs = (row, col, prev_height, coords) => {
    const key = `${row}-${col}`;
    console.log(coords);
    if (row < 0 || row === rows || col < 0 || col === cols) return;
    if (coords.has(key)) return;

    const height = heights[row][col];
    if (height < prev_height) return; // water can't flow to the ocean if prev_height is higher than current height

    coords.add(key, true);
    for (const [dr, dc] of directions) {
      dfs(row + dr, col + dc, height, coords);
    }
  };

  // for top row
  const pacific = new Set();
  const atlantic = new Set();
  for (let col = 0; col < cols; col++) {
    dfs(0, col, 0, pacific);
    dfs(rows - 1, col, 0, atlantic);
  }

  // for left row
  for (let row = 0; row < rows; row++) {
    dfs(row, 0, 0, pacific);
    dfs(row, cols - 1, 0, atlantic);
  }
  const result = [];
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (pacific.has(`${row}-${col}`) && atlantic.has(`${row}-${col}`)) {
        result.push([row, col]);
      }
    }
  }
  return result;
};

console.log(
  pacificAtlantic([
    [3, 3, 3, 3, 3, 3],
    [3, 0, 3, 3, 0, 3],
    [3, 3, 3, 3, 3, 3],
  ])
);
