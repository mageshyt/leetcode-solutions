`Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.`;

const count_less_than = (matrix, target) => {
  let row = matrix.length;
  let col = matrix[0].length;
  let count = 0;
  for (let i = 0; i < row; i++) {
    for (let j = col - 1; j >= 0; j--) {
      const current = matrix[i][j];
      if (current <= target) {
        //! once we found the the curr ent number is less than target, we can stop the loop
        count += j + 1;
        break;
      }
    }
  }
  return count;
};

const kthSmallest = (matrix, k) => {
  let row = matrix.length;
  let col = matrix[0].length;
  let left = matrix[0][0]; //! min value
  let right = matrix[row - 1][col - 1]; //! max value because the matrix is sorted

  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    const count = count_less_than(matrix, mid);
    if (count >= k) right = mid;
    else left = mid + 1;
  }
  return left;
};

console.log(
  kthSmallest(
    [
      [1, 5, 9],
      [10, 11, 13],
      [12, 13, 15],
    ],
    8
  )
);
