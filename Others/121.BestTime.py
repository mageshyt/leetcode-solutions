

def maxProfit(prices):
    left = 0 #Buy
    right = 1 #Sell
    max_profit = 0
    while right < len(prices):
        currentProfit = prices[right] - prices[left] #our current Profit
        if prices[left] < prices[right]:
            max_profit =max(currentProfit,max_profit)
        else:
            left = right
        right += 1
    return max_profit
prices=[3,4,1,6]
print(maxProfit(prices))
