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
  const map = new Map();
  for (let num of nums) {
    map.set(num, true);
  }
  for (let i = 1; i <= nums.length; i++) {
    if (!map.has(i)) {
      return i;
    }
  }
  return nums.length + 1;
};

console.log(firstMissingPositive([1, 2, 0]));
console.log(firstMissingPositive([3, 4, -1, 1]));

console.log({ ans: firstMissingPositive([7, 8, 9, 11, 12]) });
