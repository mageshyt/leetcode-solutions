`You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 1 1 2 3 3 20

`;

const sum = (nums) => {
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
  }
  return sum;
};

const minOperations = (nums, x) => {
  let target = sum(nums) - x;

  let window_sum = 0;

  let max_length = -1;

  let left = 0;
  let right = 0;
  for (left = 0, right = 0; right < nums.length; right++) {
    window_sum += nums[right];
    console.log("window_sum", window_sum, target);
    while (window_sum > target && left <= right) {
      window_sum -= nums[left++];
    }
    if (window_sum === target) {
      max_length = Math.max(max_length, right - left + 1);
    }
  }
  return max_length === -1 ? -1 : nums.length - max_length;
};
console.log(minOperations([1, 1, 4, 2, 3], 5));
