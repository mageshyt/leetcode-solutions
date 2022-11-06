`Given an m x n grid
 of characters board and a string word,
  return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
`;

const exist = (board, word) => {
  const directions = [
    [1, 0], // Right
    [-1, 0], // Left
    [0, 1], // up
    [0, -1], // down
  ];
  const rows = board.length;
  const cols = board[0].length;
  const visited = new Map();

  const dfs = (row, col, index) => {
    // base case
    if (index === word.length) return true;

    // check if the current cell is out of bounds or if the current cell is not equal to the current letter in the word

    //! case one  - out of bounds for row

    if (row < 0 || row >= rows) return false;

    //! case two - out of bounds for col

    if (col < 0 || col >= cols) return false;

    //! case three - the current cell is not equal to the current letter in the word

    if (board[row][col] !== word[index]) return false;

    // check if the current cell has been visited before
    if (visited.has(`${row}-${col}`)) return false;

    // mark the current cell as visited
    visited.set(`${row}-${col}`, true);
    // explore the neighbors of the current cell
    let result;
    for (const [rowOffset, colOffset] of directions) {
      const nextRow = row + rowOffset;
      const nextCol = col + colOffset;
      result = dfs(nextRow, nextCol, index + 1);
    }
    //! remove
    visited.delete(`${row}-${col}`);
    return result;
  };

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (dfs(i, j, 0)) {
        return true;
      }
    }
  }
  return false;
};
(board = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"],
]),
  (word = "SEE");
console.log(exist(board, "ABCPED"));
