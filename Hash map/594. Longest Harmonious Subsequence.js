`We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0
`;

const findLHS = (nums) => {
  const map = new Map();

  for (let num of nums) {
    map.set(num, map.get(num) + 1 || 1);
  }
  const keys = Array.from(map.keys());
  keys.sort((a, b) => a - b);
  let max_len = 0;
  for (let i = 0; i < keys.length; i++) {
    if (keys[i + 1] - keys[i] === 1) {
      max_len = Math.max(max_len, map.get(keys[i]) + map.get(keys[i + 1]));
    }
  }
  return max_len;
};

console.log(findLHS([1, 3, 2, 2, 5, 2, 3, 7]));
