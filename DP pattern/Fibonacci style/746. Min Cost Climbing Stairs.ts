// top down
const minCostClimbingStairs = (cost: number[]) => {
  const map = new Map<number, number>(); // key: index, value: min cost to reach the top

  const helper = (index: number): number => {
    if (index >= cost.length) return 0;

    // if we have already calculated the min cost for this index, return it
    if (map.has(index)) return map.get(index)!;
    // now calculate the min cost for this index (either we can take 1 step or 2 steps)

    const oneStep = cost[index] + helper(index + 1);
    const twoSteps = cost[index] + helper(index + 2);

    const minCost = Math.min(oneStep, twoSteps);

    // store the min cost for this index
    map.set(index, minCost);

    return minCost;
  };

  return Math.min(helper(0), helper(1));
};

// bottom up

const minCostClimbingStairs2 = (cost: number[]) => {
  const map = new Map<number, number>(); // key: index, value: min cost to reach the top

  const helper = (index: number): number => {
    // if we have already calculated the min cost for this index, return it
    if (map.has(index)) return map.get(index)!;
    // first we can tike 1 step or 2 steps so cost is 0
    if (index < 0) return 0;

    if (index === 0 || index === 1) return cost[index];

    // now calculate the min cost for this index (either we can take 1 step or 2 steps)

    const oneStep = cost[index] + helper(index - 1);
    const twoSteps = cost[index] + helper(index - 2);

    const minCost = Math.min(oneStep, twoSteps);

    // store the min cost for this index
    map.set(index, minCost);

    return minCost;
  };

  return Math.min(helper(cost.length - 1), helper(cost.length - 2));
};
const cost = [10, 15, 20];
console.log(minCostClimbingStairs(cost));

// tabulation

const minCostClimbingStairs3 = (cost: number[]) => {
  const dp = new Array(cost.length + 1).fill(0);
  dp[0] = cost[0];
  dp[1] = cost[1];

  for (let i = 2; i <= cost.length; i++) {
    dp[i] = Math.min(dp[i - 1], dp[i - 2]) + cost[i];
  }

  return Math.min(dp[cost.length - 1], dp[cost.length - 2]);
};

const cost2 = [10, 15, 20];

console.log(minCostClimbingStairs2(cost2));
