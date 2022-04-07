`Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.`;

const intersection = (nums_1, nums_2) => {
  const hash = new Map();
  const result = new Set();
  for (let char of nums_1) {
    if (!hash.get(char)) {
      // set if the char was not in the hash
      hash.set(char, true);
    }
  }
  for (let char of nums_2) {
    if (hash.get(char)) {
      result.add(char);
    }
  }

  return [...result];
};
(nums1 = [4, 9, 5]), (nums2 = [9, 4, 9, 8, 4]);
intersection(nums1, nums2);
