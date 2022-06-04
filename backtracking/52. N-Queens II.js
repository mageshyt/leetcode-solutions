`The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1`;

const totalNQueens = (n) => {
  const cols = new Set();
  const pos_diag = new Set(); // positive diagonal --> (r+c)
  const neg_diag = new Set(); // negative diagonal --> (r-c)

  let res = 0;

  const board = new Array(n).fill(0).map((_) => new Array(n).fill("."));
  const backtracking = (row, board) => {
    if (row === n) {
      res++;

      return;
    }

    for (let col = 0; col < n; col++) {
      const pos_diag_val = row + col;
      const neg_diag_val = row - col;
      if (
        cols.has(col) ||
        pos_diag.has(pos_diag_val) ||
        neg_diag.has(neg_diag_val)
      )
        continue;

      if (
        !cols.has(col) &&
        !pos_diag.has(pos_diag_val) &&
        !neg_diag.has(neg_diag_val)
      ) {
        cols.add(col);
        pos_diag.add(pos_diag_val);
        neg_diag.add(neg_diag_val);
        board[row][col] = "Q";
      }
      backtracking(row + 1, [...board]);
      cols.delete(col);
      pos_diag.delete(pos_diag_val);
      neg_diag.delete(neg_diag_val);
      board[row][col] = ".";
    }
  };

  backtracking(0, board);
  return res;
};

console.log(totalNQueens(4));
