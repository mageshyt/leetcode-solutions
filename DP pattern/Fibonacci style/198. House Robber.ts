// top down
const rob = (nums: number[]): number => {
  const map = new Map<number, number>(); // key: index, value: max profit

  const helper = (index: number): number => {
    if (index >= nums.length) return 0;

    if (map.has(index)) return map.get(index)!;

    const robCurrentHouse = nums[index] + helper(index + 2);

    const skipCurrentHouse = helper(index + 1);

    const maxProfit = Math.max(robCurrentHouse, skipCurrentHouse);

    map.set(index, maxProfit);

    return maxProfit;
  };

  return helper(0);
};

// tabulation

const rob2 = (nums: number[]): number => {
  const dp = new Array(nums.length + 1).fill(0); // dp[i] = max profit we can get from house i to the end

  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i <= nums.length; i++) {
    dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
  }

  return dp[nums.length - 1];
};

// tabulation with O(1) space

const nums = [1, 2, 3, 1];

console.log(rob([2, 1]));

console.log(rob2(nums));
