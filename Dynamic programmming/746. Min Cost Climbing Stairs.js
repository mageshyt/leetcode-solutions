`You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.`;

//! tabulation
const minCostClimbingStairs = (cost) => {
  const table = new Array(cost.length + 1).fill(0);
  table[0] = 0;
  table[1] = 0;
  for (let i = 2; i <= cost.length; i++) {
    table[i] = Math.min(table[i - 1] + cost[i - 1], table[i - 2] + cost[i - 2]);
  }
  return table[cost.length];
};

//! memo and recur
const minCostClimbingStairs2 = (cost) => {
  const memo = new Map();
  const length = cost.length;
  const helper = (i) => {
    if (memo.has(i)) return memo.get(i);
    if (i < 0) return 0;
    if (i === 0 || i === 1) return cost[i];
    const res = cost[i] + Math.min(helper(i - 1), helper(i - 2));
    memo.set(i, res);
    return res;
  };
  return Math.min(helper(length - 1), helper(length - 2));
};
console.log(minCostClimbingStairs2([10, 15, 20]));
