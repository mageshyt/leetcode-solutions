`Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1`;

const firstMissingPositive = (nums) => {
  //! sort the nums
  nums.sort((a, b) => a - b);
  //! check if the first element is positive
  for (let i = 0; i < nums.length; i++) {
    const curr = nums[i];
    if (nums[i] < 0) {
      continue;
    }
    if (curr + 1 === nums[i + 1]) {
      continue;
    } else {
      return curr + 1;
    }
  }
};

console.log(firstMissingPositive([1, 2, 0]));
console.log(firstMissingPositive([3, 4, -1, 1]));
console.log(firstMissingPositive([7, 8, 9, 11, 12]));
