`An integer array is called arithmetic if it consists of at
 least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0`;

const numberOfArithmeticSlices = (nums) => {
  let count = 0;
  let arithmetic_subarrays_count = 0;
  for (let i = 0; i < nums.length; i++) {
    const difference_1 = nums[i] - nums[i + 1]; // ! getting difference between two consecutive numbers
    const difference_2 = nums[i + 1] - nums[i + 2]; // ! getting difference between next two consecutive number
    if (difference_1 === difference_2) {
      count++;
      arithmetic_subarrays_count += count;
    } else {
      count = 0;
    }
  }

  return arithmetic_subarrays_count;
};
console.log(numberOfArithmeticSlices([1, 3, 5, 7, 9]));
