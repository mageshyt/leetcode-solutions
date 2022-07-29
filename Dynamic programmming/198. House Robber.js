`You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.`;
const RobTheBob = (nums) => {
  let bob1 = 0;
  let bob2 = 0;
  for (let i = 0; i < nums.length; i++) {
    const houses = nums[i];
    const temp = Math.max(bob1 + houses, bob2);
    bob1 = bob2;
    bob2 = temp;
  }

  return bob2;
};

// console.log(RobTheBob([2, 7, 9, 3, 1]));

`
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
`;

var climbStairs = function (n) {
  let step_1 = 1;
  let step_2 = 1;
  for (let i = 0; i < n; i++) {
    const temp = step_1;
    step_1 += step_2;
    step_2 = temp;

    console.log({ step_1, step_2, temp });
  }

  return step_2;
};

// console.log(climbStairs(5));

//! bottom up steps
const RobTheBob2 = (nums) => {
  if (nums.length == 1) return nums[0];
  const rob_amt = new Array(nums.length + 1).fill(0);

  rob_amt[0] = nums[0];
  rob_amt[1] = Math.max(nums[0], nums[1]);
  
  for (let i = 2; i < nums.length; i++) {
    rob_amt[i] = Math.max(rob_amt[i - 1], rob_amt[i - 2] + nums[i]);
  }
  return rob_amt[nums.length - 1];
};

// console.log(RobTheBob2([2, 7, 9, 3, 1]));
// console.log(RobTheBob2([1, 2, 3, 1]));
console.log(RobTheBob2([2, 1, 1, 2]));
