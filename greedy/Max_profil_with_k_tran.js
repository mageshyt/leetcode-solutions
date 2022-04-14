`Max Profit With K Transactions
You're given an array of positive integers representing the prices of a single stock on various days (each index in the array represents a
different day). You're also given an integer k, which represents the number of transactions you're allowed to make. One transaction
consists of buying the stock on a given day and selling it on another, later day.
Write a function that returns the maximum profit that you can make by buying and selling the stock, given k transactions.
Note that you can only hold one share of the stock at a time; in other words, you can't buy more than one share of the stock on any
given day, and you can't buy a share of the stock if you're still holding another share. Also, you don't need to use all k transactions that
you're allowed.
Sample Input
 prices = [5, 11, 3, 50, 60, 90]
k = 2
Sample Output
 93 // Buy: 5, Sell: 11; Buy: 3, Sell: 90`;

const maxProfitWithKTransactions = (prices, k) => {
  if (!prices.length) return 0;
  const profits = new Array(k + 1).fill(new Array(prices.length).fill(0));
  `
  t--> transaction
  d--> day
  `;
  for (let t = 1; t < k + 1; t++) {
    let maxProfit = -Infinity;
    for (let day = 1; day < prices.length; day++) {
      maxProfit = Math.max(
        maxProfit,
        profits[t - 1][day - 1] - prices[day - 1]
      );
      profits[t][day] = Math.max(profits[t][day - 1], maxProfit + prices[day]);
    }
  }
  return profits[k][prices.length - 1];
};
console.log(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2));
