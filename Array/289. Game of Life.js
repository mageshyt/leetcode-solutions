`According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]`;

const gameOfLife = (board) => {
  // Corresponding to [N, NE, E, SE, S, SW, W, NW]
  directions = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
  ];
  const rows = board.length;
  const cols = board[0].length;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      let liveNeighbors = 0;
      //! search in 8 directions
      for (let k = 0; k < directions.length; k++) {
        let x = i + directions[k][0];
        let y = j + directions[k][1];
        if (x >= 0 && x < rows && y >= 0 && y < cols) {
          if (board[x][y] === 1 || board[x][y] === 2) {
            liveNeighbors++;
          }
        }
      }
      if (board[i][j] === 1) {
        if (liveNeighbors < 2 || liveNeighbors > 3) {
          board[i][j] = 2;
        }
      } else if (liveNeighbors === 3) {
        board[i][j] = 3;
      }
    }
  }
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (board[i][j] === 2) {
        board[i][j] = 0;
      } else if (board[i][j] === 3) {
        board[i][j] = 1;
      }
    }
  }
  console.table(board);
  return board;
};
console.log(
  gameOfLife([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
  ])
);
