`Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
`;

const generate = (numRows) => {
  const genResult = []; //! our result that we will return
  genResult.push([1]); //! push the first row
  for (let i = 1; i < numRows; i++) {
    let row = [1]; // we are adding out first boundry element
    for (let j = 1; j < i; j++) {
      row.push(genResult[i - 1][j - 1] + genResult[i - 1][j]);
      `
      [1]
      [1,1]
     [1,2,1]
        generateResult [i-1][j-1] will give 2 row and  and first element of that row is 1
    [1,3,3,1]
      `;
    }
    row.push(1); //! we will add our end boundry element
    genResult.push(row);
  }
  return genResult;
};
console.log(generate(5));
