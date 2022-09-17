  for (let i = 1; i < prices.length; i++) {
    const buy = prices[i];
    const sell = prices[i - 1];
    const profit = buy - sell;

    if (k > 0 && profit > 0) {
      maxProfit.push(profit);
      k--;
    }
  }
  return maxProfit.reduce((a, b) => a + b, 0);