`You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
 
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.`;

const maxProfit = (prices) => {
  let current_profit = 0;
  let min_so_far = prices[0];

  for (let i = 0; i < prices.length; i++) {
    const curr_price = prices[i];
    min_so_far = Math.min(min_so_far, curr_price);
    const profit = curr_price - min_so_far;
    current_profit = Math.max(current_profit, profit);
    // console.log({ curr_price, prev_price, profit, current_profit, min_so_far });
    console.log(
      `profit 👉 curr_price -->${curr_price} - min_price-->${min_so_far} = ${profit}`
    );
    // console.log(`current_profit 👉 ${current_profit}`);
  }
  console.log(`profit
     --> {current_profit }`)
 
  return current_profit;
  
};
console.log(maxProfit([7, 1, 5, 3, 6, 4]));

