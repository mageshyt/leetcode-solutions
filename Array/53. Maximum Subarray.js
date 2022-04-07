`
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
`;
const sum = (array) => {
  let total = 0;
  for (let i = 0; i < array.length; i++) {
    total += array[i];
  }
  return total;
};
const maxSubArray = (array) => {
  let max_Sum = array[0];
  let current_Sum = max_Sum;
  for (let i = 1; i < array.length; i++) {
    const current = array[i];
    current_Sum = Math.max(current_Sum + current, array[i]);
    max_Sum = Math.max(current_Sum, max_Sum);
  }
  return max_Sum;
};
nums = [5, 4, -1, 7, 8];
console.log(maxSubArray(nums));
//  sum all nums in array
