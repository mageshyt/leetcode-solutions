`You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3`;
const helper = (nums, len) => {
  let rob1_earn = 0;
  let rob2_earn = 0;
  for (let i = 0; i < len; i++) {
    let new_Rob_Amount = Math.max(rob1_earn + nums[i], rob2_earn);
    // console.log("before");
    // console.log({ new_Rob_Amount, rob1_earn, rob2_earn });
    rob1_earn = rob2_earn;
    rob2_earn = new_Rob_Amount;
    // console.log("after");
    // console.log({ new_Rob_Amount, rob1_earn, rob2_earn });
  }
  return rob2_earn;
};
const rob = (nums) => {
  max_amount = Math.max(
    helper(nums.slice(1), nums.length - 1),
    helper(nums.slice(0, nums.length - 1), nums.length - 1)
  );
  return Math.max(nums[0], max_amount);
};
console.log(rob([2, 3, 2]));
console.log(rob([1, 2, 3, 1]));
