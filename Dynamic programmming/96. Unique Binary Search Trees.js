`Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1`;
const numTrees = (n) => {
  const table = new Array(n + 1).fill(0);
  table[0] = 1;
  table[1] = 1; //! we will first of first 2 elements as 1
  for (let i = 2; i <= n; i++) {
    for (let j = 1; j <= i; j++) {
      table[i] += table[j - 1] * table[i - j]; //! we are using table latino to calculate the number of unique BST's
    }
  }
  return table[n];
};

console.log(numTrees(3));
