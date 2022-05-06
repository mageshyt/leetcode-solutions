`Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4]`;

const intersection = (nums) => {
  const hash = new Map();

  for (let i = 0; i < nums.length; i++) {
    const map = new Map();
    for (let j = 0; j < nums[i].length; j++) {
      if (!map.has(nums[i][j])) {
        map.set(nums[i][j], 1);
      } else {
        map.set(nums[i][j], map.get(nums[i][j]) + 1);
      }
    }
    for (let [key, value] of map) {
      if (!hash.has(key)) {
        hash.set(key, value);
      } else {
        hash.set(key, hash.get(key) + value);
      }
    }
  }
  return [...hash.keys()].filter((key) => hash.get(key) === nums.length);
};

console.log(
  intersection([
    [3, 1, 2, 4, 5],
    [1, 2, 3, 4],
    [3, 4, 5, 6],
  ])
);
