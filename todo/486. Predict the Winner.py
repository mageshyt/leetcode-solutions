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

from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        cache = {}  # Create a dictionary to store the results of subproblems.

        # The `helper` function calculates the maximum score that can be achieved by the current player
        # by choosing numbers from the subarray nums[i:j+1], where i is the starting index and j is the ending index.

        def helper(i, j):
            # Check if the result for the current subarray (i, j) is already in the cache.
            if (i, j) in cache:
                return cache[(i, j)]

            # Base cases:
            if i == j:
                return nums[i]  # If there is only one element in the subarray, return its value.

            if i > j:
                return 0  # If i is greater than j, the subarray is empty, so return 0.

            # Calculate the maximum score that can be achieved by the current player by choosing the first or last element
            # of the subarray, and then recursively calculating the minimum score that the other player can achieve
            # with the remaining subarray after the current player's turn.
            max_score = max(
                nums[i] + min(helper(i + 2, j), helper(i + 1, j - 1)),
                nums[j] + min(helper(i + 1, j - 1), helper(i, j - 2))
            )

            # Store the result in the cache.
            cache[(i, j)] = max_score

            return max_score

        # Calculate Bob's maximum score.
        bob_score = helper(0, n - 1)

        print(bob_score)  # Print Bob's maximum score.

        # Calculate the total sum of all the numbers in the array.
        total = sum(nums)

        # Alice's maximum score is the total sum of all the numbers in the array minus Bob's maximum score.
        alice_score = total - bob_score

        return bob_score >= alice_score  # Return True if Bob's maximum score is greater than or equal to Alice's maximum score, otherwise return False.


if __name__ == "__main__":
    print(Solution().PredictTheWinner([1,5,233,7]))

