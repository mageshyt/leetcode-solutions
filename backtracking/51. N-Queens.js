`The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]`;

const solveNQueens = (n) => {
  const cols = new Set();
  const pos_diag = new Set(); // positive diagonal --> (r+c)
  const neg_diag = new Set(); // negative diagonal --> (r-c)

  const res = [];

  const board = new Array(n).fill(0).map((_) => new Array(n).fill("."));
  const dfs = (row, board) => {
    if (row === n) {
      res.push(board.map((row) => row.join("")));

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
      dfs(row + 1, [...board]);
      cols.delete(col);
      pos_diag.delete(pos_diag_val);
      neg_diag.delete(neg_diag_val);
      board[row][col] = ".";
    }
  };
  dfs(0, board);
  return res;
};

console.log(solveNQueens(4));
