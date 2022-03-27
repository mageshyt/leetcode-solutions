`Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127`;

const findMaxXOR = (nums) => {
  let max_XOR = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      max_XOR = Math.max(max_XOR, nums[i] ^ nums[j]);
    }
  }

  return max_XOR;
};

nums = [8, 10, 2];
findMaxXOR(nums);
