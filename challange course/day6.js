`1588. Sum of All Odd Length Subarrays

Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

 

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
`;
const sum = (arr) => {
  let sum = 0;
  for (let num of arr) {
    sum += num;
  }
  return sum;
};
const sumOddLengthSubarrays = (arr) => {
  let sum = 0;
  
};
console.log(sumOddLengthSubarrays([1, 4, 2, 5, 3]));
`283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
`;
const moveZeroes = (nums) => {
  let i = 0;
  let r = 0;
  while (i < nums.length) {
    if (nums[i] !== 0) {
      nums[r] = nums[i];
      r++;
    }
    i++;
  }
  while (r < nums.length) {
    nums[r] = 0;
    r++;
  }

  return nums;
};
console.log(moveZeroes([0, 1, 0, 3, 12]));

`1672. Richest Customer Wealth
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.


`;

const maximumWealth = (nums) => {
  let max = 0;
  for (let amt of nums) {
    const sum = amt.reduce((a, b) => a + b);
    max = Math.max(max, sum);
  }
  return max;
};

// console.log(
//   maximumWealth([
//     [1, 2, 3],
//     [3, 2, 1],
//   ])
// );
