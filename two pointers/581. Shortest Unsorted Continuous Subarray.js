`Given an integer array nums, 
you need to find one continuous subarray that if you only sort this subarray in ascending order,
 then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0`;

const findUnsortedSubarray = (nums) => {
  let end = -1;

  let max = nums[0];
  let min = nums[nums.length - 1];
  let start = 0;
  for (let i = 1; i < nums.length; i++) {
    max = Math.max(max, nums[i]);
    if (max > nums[i]) {
      end = i;
    }
  }
  for (let i = nums.length - 2; i >= 0; i--) {
    min = Math.min(min, nums[i]);
    if (min < nums[i]) {
      start = i;
    }
  }
  return end - start + 1;
};

console.log(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]));
