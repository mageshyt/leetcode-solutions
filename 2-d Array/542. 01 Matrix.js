`Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
`;

const updateMatrix = (matrix) => {
  const directions = [
    [0, 1], // up
    [0, -1], // down
    [1, 0], // Right
    [-1, 0], // Left
  ];
  const visited = new Map();
  const rows = matrix.length;
  const cols = matrix[0].length;
  const queue = [];
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (matrix[r][c] === 0) {
        queue.push([r, c]);
      }
    }
  }
  console.log(queue);
  while (queue.length) {
    const [r, c] = queue.shift();
    for (let [dr, dc] of directions) {
      const newRow = r + dr;
      const newCol = c + dc;
      if (
        newRow >= 0 &&
        newRow < rows &&
        newCol >= 0 &&
        newCol < cols &&
        matrix[newRow][newCol] === 1 &&
        !visited.get(`${newRow}-${newCol}`)
      ) {
        queue.push([newRow, newCol]);
        visited.set(`${newRow}-${newCol}`, true);
        matrix[newRow][newCol] = matrix[r][c] + 1;
      }
    }
  }
  return matrix;
};
mat = [
  [0, 0, 0],
  [0, 1, 0],
  [1, 1, 1],
];
console.log(updateMatrix(mat));
