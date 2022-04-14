`Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]`;

const wiggleSort = (nums) => {
  const len = nums.length;
  for (let i = 0; i < len; i++) {
    const first = nums[i];
    const next = nums[i + 1];
    if (first < next) {
      i++;
      continue;
    } else {
      for (let j = i + 1; j < len; j++) {
        if (nums[j] > first) {
          [nums[i + 1], nums[j]] = [nums[j], nums[i + 1]];
          break;
        }
      }
    }
  }
  return nums;
};
console.log(wiggleSort([1, 5, 1, 1, 6, 4]));
