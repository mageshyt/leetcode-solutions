const generateMatrix = (n) => {
  // create matrix
  const matrix = new Array(n).fill().map(() => new Array(n).fill(0));
  // Define our pointer rows and columns
  let row = 0;
  let column = 0;
  let dir = 0;
  // !directions
  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  for (let i = 0; i < n * n; i++) {
    matrix[row][column] = i + 1;
    //! temp variable to store next row and column
    let tempNextRow = row + directions[dir][0];
    let tempNextColumn = column + directions[dir][1];
    // ! Check if matrix is out of bound or if we already visited that element
    if (
      matrix[tempNextRow] === undefined ||
      matrix[tempNextRow][tempNextColumn] === undefined ||
      matrix[tempNextRow][tempNextColumn] !== 0
    ) {
      dir = (dir + 1) % 4;
      // ! Move to the next direction
    }
    row += directions[dir][0]; //!  Move to the next row
    column += directions[dir][1]; //!  Move to the next column
  }
  return matrix;
};
