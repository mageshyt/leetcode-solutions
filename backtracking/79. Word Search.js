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
    if (index === word.length) {
      return true;
    }
    const key = `${row}-${col}`;
    if (
      row < 0 ||
      row >= rows ||
      col < 0 ||
      col >= cols ||
      board[row][col] !== word[index] ||
      visited.get(key)
    )
      return false;
    visited.set(key, true);
    //! going to all the directions to check if the word exists
    const res =
      dfs(row + 1, col, index + 1) ||
      dfs(row - 1, col, index + 1) ||
      dfs(row, col + 1, index + 1) ||
      dfs(row, col - 1, index + 1);

    visited.delete(key);
    return res;
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

console.log(
  exist(
    [
      ["A", "B", "C", "E"],
      ["S", "F", "C", "S"],
      ["A", "D", "E", "E"],
    ],
    "ABCCED"
  )
);
