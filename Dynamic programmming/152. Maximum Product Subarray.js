`Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.`;

const maxProduct = (nums) => {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  let max = nums[0];
  let prev_max = nums[0];
  let pre_min = nums[0];
  for (let i = 1; i < nums.length; i++) {
    const curr = nums[i];
    const prev_max_temp = prev_max;
    `
    p_max=max(3,max(6,6)) --> 6
    p_min=min(3,min(6,6)) --> 3
    `;
    prev_max = Math.max(curr, Math.max(prev_max_temp * curr, pre_min * curr));
    pre_min = Math.min(curr, Math.min(prev_max_temp * curr, pre_min * curr));
    max = Math.max(max, prev_max);
    // console.log({ prev_max, pre_min, max });
  }
  return max;
};

console.log(maxProduct([2, 3, -2, 4]));
