`Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
 

Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]`;
const countKDifference = (nums, k) => {
  const map = new Map();
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    map.set(nums[i], map.get(nums[i]) + 1 || 1);
  }
  for (let num of nums) {
    if (map.has(num + k)) {
      count += map.get(num + k);
    }
  }
  return count;
};
console.log(countKDifference([1, 2, 2, 1], 1));
