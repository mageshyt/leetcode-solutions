`Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

 

Example 1:


Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.
Example 2:


Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.`;
const count_less_than = (mid, row, col) => {
  let count = 0;
  for (let i = 1; i < row + 1; i++) {
    count += Math.min(Math.floor(mid / i), col);
  }
  return count;
};

const findKthNumber = (k, m, n) => {
  let row = m;
  let col = n;
  let left = 1;
  let right = m * n;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    const count = count_less_than(mid, row, col);
    if (count >= k) right = mid;
    else left = mid + 1;
  }
  return left;
};

console.log(findKthNumber(5, 3, 3));

console.log(findKthNumber(6, 2, 3));
