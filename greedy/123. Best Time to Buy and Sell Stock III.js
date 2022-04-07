`You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.`;

const maxProfit = (prices) => {
  let stock1 = Infinity;
  let stock2 = Infinity;
  let stock1_profit = -Infinity;
  let stock2_profit = -Infinity;
  for (let i = 0; i < prices.length; i++) {
    `
      1.we are calculating the stock when we bought it.
      2.we are calculating the stock when we sold it. --> update out stock1_profit.
      3. we are calculating the stock2 when we bought it. by curr - stock1_profit. 
    4. we are calculating the stock2 when we sold it. --> update out stock2_profit = -Infinity;. max(stock2_profit = -Infinity;, curr - stock2)
      `;
    stock1 = Math.min(stock1, prices[i]);
    stock1_profit = Math.max(stock1_profit, prices[i] - stock1);
    stock2 = Math.min(stock2, prices[i] - stock1_profit);
    stock2_profit = Math.max(stock2_profit, prices[i] - stock2);
  }
  return stock2_profit;
};
console.log(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]));
console.log(maxProfit([1, 2, 3, 4, 5]));
console.log(maxProfit([7, 6, 4, 3, 1]));
