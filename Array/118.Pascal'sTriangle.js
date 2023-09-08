`Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:
    1 <= numRows <= 30
    
`;
const generate = (numRows) => {
  const result = [];
  for (let i = 0; i < numRows; i++) {
    result.push([]);
    for (let j = 0; j <= i; j++) {
      if (j === 0 || j === i) {
        //! first and last element going to be 1
        result[i].push(1);
      } else {
        //! middle elements are the sum of the two above elements (i-1, j-1) and (i-1, j)
        result[i].push(result[i - 1][j - 1] + result[i - 1][j]);
      }
    }
  }
  return result;
};

console.log(generate(100));
