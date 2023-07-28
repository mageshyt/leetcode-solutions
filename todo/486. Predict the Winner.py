"""You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

 

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.
Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win."""
from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]  # Create a 2D array to store the results of subproblems.

        # Fill in the dp array from the bottom up.
        for i in range(n-1, -1, -1):  # Iterate from the end of the array to the beginning.
            for j in range(i, n):  # For each element i, calculate the result for all possible subarrays ending at index j.
                if i == j:  # Base case: If i and j are the same, there is only one element in the subarray.
                    dp[i][j] = nums[i]  # So, the result is simply the value of that element.
                else:
                    # For other cases, calculate the result by choosing the maximum of two options:
                    # 1. If the player chooses the element at index i, subtract the result of the subarray excluding that element (dp[i+1][j]).
                    # 2. If the player chooses the element at index j, subtract the result of the subarray excluding that element (dp[i][j-1]).
                    dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])

        return dp[0][n-1] >= 0  # The final result will be stored at dp[0][n-1], and we check if it is greater than or equal to 0.
