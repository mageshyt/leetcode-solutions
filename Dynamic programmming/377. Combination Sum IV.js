`Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
`;

const combinationSum4 = (nums, target) => {
  const dp = new Map();
  dp.set(0, 1);

  const dfs = (target) => {
    if (dp.has(target)) return dp.get(target);
    let target_count = 0;

    for (let num of nums) {
      if (target > num) {
        target_count += dfs(target - num);
      } else if (target === num) {
        target_count++;
      }
    }
    dp.set(target, target_count);
    return target_count;
  };
  return dfs(target);
};
console.log(combinationSum4([1, 2, 3], 4));
