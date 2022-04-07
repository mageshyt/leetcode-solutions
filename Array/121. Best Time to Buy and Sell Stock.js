`
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

  Input: prices = [7,6,4,3,1]
co
Output: 0
// Explanation: In this case, no transactions are done and the max profit = 0.`;

const max_profit = (prices) => {
  let current_max = 0;
  let max_so_far = 0;
  for (let i = 1; i < prices.length; i++) {
    current_max = Math.max(0, current_max + prices[i] - prices[i - 1]);
    max_so_far = Math.max(max_so_far, current_max);
  }
  return max_so_far;
};

prices = [7, 1, 5, 3, 6, 4];
console.log(max_profit(prices));
