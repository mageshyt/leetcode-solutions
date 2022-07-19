`iven a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0
 

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
Accepted
70,069
Submissions
101,614`;

const numSubmatrixSumTarget = (M, T) => {
  let row = M[0].length;
  let col = M.length;
  let ans = 0;
  let res = new Map();
  let currentSum = 0;
  for (let i = 0, r = M[0]; i < col; r = M[++i])
    for (let j = 1; j < row; j++) r[j] += r[j - 1];

  for (let j = 0; j < row; j++)
    for (let k = j; k < row; k++) {
      res.clear(), res.set(0, 1), (currentSum = 0); // reset the current sum and the map
      for (let i = 0; i < col; i++) {
        currentSum += M[i][k] - (j ? M[i][j - 1] : 0); // update the current sum
        ans += res.get(currentSum - T) || 0; // update the answer
        res.set(currentSum, (res.get(currentSum) || 0) + 1); // update the map
      }
    }
  return ans;
};

console.log(
  numSubmatrixSumTarget(
    [
      [0, 1, 0],
      [1, 1, 1],
      [0, 1, 0],
    ],
    0
  )
);
