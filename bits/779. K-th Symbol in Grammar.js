`We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
Example 2:

Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01`;

const kthGrammar = (n, k) => {
  let left = 1; // Left boundary
  let right = 2 ** (n - 1); // Right boundary of the string for the current level
  let res = 0;

  for (let i = 0; i < n - 1; i++) {
    let mid = Math.floor((left + right) / 2); // Find the middle position of the string

    if (k <= mid) {
      // if k is in the left half, adjust the right boundary
      right = mid;
    } else {
      left = mid + 1; // If k is in the right half, adjust the left boundary
      res = res === 0 ? 1 : 0; // Toggle the current character (0 to 1, or 1 to 0)
    }
  }

  return res;
};
