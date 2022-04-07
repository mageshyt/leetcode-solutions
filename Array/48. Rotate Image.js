`You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 `;
const rotate = (matrix) => {
  //! initialize pointer
  let left_pointer = 0;
  let right_pointer = matrix.length - 1;

  while (left_pointer < right_pointer) {
    for (let i = 0; i < right_pointer - left_pointer; i++) {
      // lets store top and bottom values
      const top = left_pointer;
      const bottom = right_pointer;
      //! lets save the top left value
      const top_left = matrix[top][left_pointer + i];
      // ! lets move bottom left to top left
      matrix[top][left_pointer + i] = matrix[bottom - i][left_pointer];
      `
        [1,2,3]
        [4,5,6]
        [7,8,9]
        here bottom left is 7 so we will move it to top left which  in the place of 
         1
        after that 
        [7,2,3]
        [4,5,6]
        [7 ,8,9]
        now we will move bottom right to bottom left right
        [7,2,3]
        [4,5,6]
        [9,8,9]

         ;
      `;
      //! move bottom right to bottom left
      matrix[bottom - i][left_pointer] = matrix[bottom][right_pointer - i];
      //! move top right to bottom right
      matrix[bottom][right_pointer - i] = matrix[top + i][right_pointer];
      //! move top left to top right
      matrix[top + i][right_pointer] = top_left; // ! this is our top left value which we store
    }
    left_pointer++;
    right_pointer--;
  }
  console.log(matrix);

};

console.log(
  rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ])
);

`Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]`;

console.log()