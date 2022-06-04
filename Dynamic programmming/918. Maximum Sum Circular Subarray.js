`Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.`;

const maxSubarraySumCircular = (nums) => {
  if (Math.max(...nums) < 0) return Math.max(...nums);

  //! to keep track max
  let max_sum = nums[0];
  let curr_max = nums[0];

  //! to keep track min

  let min_sum = nums[0];
  let curr_min = nums[0];
  for (let i = 1; i < nums.length; i++) {
    const curr_max_sum = nums[i] + curr_max;
    curr_max = Math.max(nums[i], curr_max_sum);
    max_sum = Math.max(max_sum, curr_max);

    curr_min = Math.min(nums[i], nums[i] + curr_min);

    min_sum = Math.min(min_sum, curr_min);
  }

  const sum = nums.reduce((a, b) => a + b);
  return Math.max(max_sum, sum - min_sum);
};
console.log(maxSubarraySumCircular([1, -2, 3, -2]));
console.log(maxSubarraySumCircular([5, -3, 5]));
