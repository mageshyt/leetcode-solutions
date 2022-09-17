`You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.`;
const maxProfit = (prices, k) => {
  if (k === 0) return 0; // ! if no prices or no transactions then return 0
  const profits = new Array(k + 1).fill([Number.MAX_SAFE_INTEGER, 0]); // ! dp[1][0] = min price, dp[1][1] = max profit
  console.log(profits);
  for (let price of prices) {
    for (let i = 1; i <= k; i++) {
      const [minPrice, maxProfit] = profits[i];
      profits[i] = [
        Math.min(minPrice, price - profits[i - 1][1]),
        Math.max(maxProfit, price - minPrice),
      ];
    }
  }

  return profits[k][1];
};

console.log(maxProfit([2, 4, 1], 2));
console.log(maxProfit([3, 2, 6, 5, 0, 3], 2));
console.log(maxProfit([3, 3, 5, 0, 0, 3, 1, 4], 2));
