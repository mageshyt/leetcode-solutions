`Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.`;

const findPairs = (nums, k) => {
  let count = 0;
  const map = new Map();
  for (let num of nums) {
    if (map.has(num)) {
      map.set(num, map.get(num) + 1);
    } else {
      map.set(num, 1);
    }
  }
  for (let num of map.keys()) {
    const current = num;
    const target = current + k;
    if ((k > 0 && map.has(target)) || (k === 0 && map.get(current) > 1)) {
      count++;
    }
  }
  return count;
};
(nums = [1, 3, 1, 5, 4]), (k = 0);
console.log(findPairs(nums, k));
