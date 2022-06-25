`Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0`;

const countBattleships = (board) => {
  let count = 0;
  const col = board[0].length;
  const row = board.length;

  // ! go col wise
  for (let c = 0; c < col; c++) {z
    for (let r = 0; r < row; r++) {
      const current_cell = board[r][c];
      if (current_cell === "X") {
        if (c - 1 >= 0 && board[r][c - 1] === "X") continue; // ! if left cell is already a battleship, skip
        if (r - 1 >= 0 && board[r - 1][c] === "X") continue; // ! if top cell is already a battleship, skip
        console.log("found a battleship", r, c);
        count++;
      }
    }
  }

  return count;
};

console.log(
  countBattleships([
    ["X", ".", ".", "X"],
    [".", ".", ".", "X"],
    [".", ".", ".", "X"],
  ])
);
