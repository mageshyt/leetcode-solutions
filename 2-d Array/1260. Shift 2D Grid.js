`
    For Example:
        k=4
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    col_len = 3
    row_len = 3

    we will take r=0,col=0 and curr num=1  and we pass the row and col to pos_to_val function
        pos_to_val(0,0) = 3*0+0+4 = 4
        so 1 need to be place in 4 index
    to get the row and col of index 4 in 1 D array
        val_to_Pos(4) = { row : floor(4/3) = 1, col : (4%3) = 1} 
        our new grid will be
        [0,0,0]
        [0,1,0]
        [0,0,0]
    
    out of bounce case :
        another example we take r=2,col=1 and curr num=8 and we pass the row and col to pos_to_val function
            pos_to_val(2,1) = (3*2)+1+4 = 11 this is out of bound so we will take modulo 11 % (3*3) = 11 % 9 = 2
            so 8 need to be place in 2 index
        to get the row and col of index 13 in 1 D array
            val_to_Pos(2) = { row : floor(2/3) = 0, col : (2%3) = 2}
            our new grid will be
            [0,0,8]
            [0,1,0]
            [0,0,0]
    you can simulate for all the elements in the grid

`;

const shiftGrid = (grid, k) => {
  const col_len = grid[0].length;
  const row_len = grid.length;
  const new_grid = new Array(row_len) //! new Grid
    .fill(0)
    .map(() => new Array(col_len).fill(0));

  const Pos_to_val = (row, col) => {
    //! we are covering the entire grid to 1 D position;
    return col_len * row + col + k;
  };

  const val_to_Pos = (val) => {
    //! converting 1 D to 2D
    return {
      row: Math.floor(val / col_len),
      col: val % col_len,
    };
  };
  for (let row = 0; row < row_len; row++) {
    for (let col = 0; col < col_len; col++) {
      const val = Pos_to_val(row, col) % (row_len * col_len); //! we are % because we should not be out of bounce
      const { row: new_row, col: new_col } = val_to_Pos(val);
      new_grid[new_row][new_col] = grid[row][col]; //! we are copying the value from old grid to new grid
    }
  }
  return new_grid;
};

console.log(
  shiftGrid(
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ],
    4
  )
);
