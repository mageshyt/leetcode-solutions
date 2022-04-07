`You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1`;

const findTargetSumWays = (nums, target) => {
  const memo = {}; // ! here we will store the index, total
  const backTrack_helper = (idx, total) => {
    //! Edge cases
    if (idx === nums.length) {
      return total === target ? 1 : 0;
    }

    //! if we have already calculated the result for this index and total then return if
    if (`${idx},${total}` in memo) {
      return memo[`${idx},${total}`];
    }
    // ! Fun part 😀
    memo[`${idx},${total}`] =
      backTrack_helper(idx + 1, total + nums[idx]) +
      backTrack_helper(idx + 1, total - nums[idx]);
    return memo[`${idx},${total}`];
  };
  return backTrack_helper(0, 0);
};

nums = [1, 1, 1, 1, 1];
target = 3;
console.log(findTargetSumWays(nums, target));
