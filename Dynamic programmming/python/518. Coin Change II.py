"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1"""
from typing import List
class Solution:
    def change(self, amount: int, denoms: List[int]) -> int:

        # Base cases
        if amount == 0:
            return 1

        if amount < 0 or len(denoms) == 0:
            return 0

        dp = [0]*(amount+1) 

        dp[0] = 1  # to make 0 we have 1 way

        for denom in denoms:
            for amt in range(denom, amount+1):

                dp[amt] += dp[amt-denom]

        return dp[-1]
    

    # solution 2

    def change(self, amount: int, denoms: List[int]) -> int:

        cache={}

        def dfs(amt):

            if amt==0:
                return 1
            
            if amt in cache:
                return cache[amt]
            
            res=amount+1

            for denom in denoms:

                for amount in range(denoms,amt+1):

                    res+=dfs(amount-denom)


            cache[amt]=res

            return cache[amt] if cache[amt] != amount+1 else 0
        

        return dfs(amount)
    

