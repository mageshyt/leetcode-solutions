`Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0`;
const threeSumClosest = (nums, target) => {
  let ans = nums[0] + nums[1] + nums[2];
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length; i++) {
    let left_pointer = i + 1;
    let right_pointer = nums.length - 1;
    while (left_pointer < right_pointer) {
      const current_sum = nums[i] + nums[left_pointer] + nums[right_pointer];
      if (current_sum > target) {
        right_pointer--;
      } else if (current_sum < target) {
        left_pointer++;
      }
      if (Math.abs(current_sum - target) < Math.abs(ans - target)) {
        ans = current_sum;
      }
    }
  }
  return ans;
};

console.log(threeSumClosest([-1, 2, 1, -4], 1));
