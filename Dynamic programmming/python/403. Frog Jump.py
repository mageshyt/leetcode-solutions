"""A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
"""


from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Check if the first jump is possible from the first stone
        if stones[1] != 1:
            return False
        
        dp = {}  # Dynamic programming memoization
        
        # Create a hashmap that stores stone values as keys and their indices as values
        indices = {v: i for i, v in enumerate(stones)}

        def dfs(lastStep, curr_idx):
            # If the current state has been calculated before, return the result from memoization
            if (lastStep, curr_idx) in dp:
                return dp[(lastStep, curr_idx)]

            # If the frog has reached the last stone, return True
            if curr_idx == len(stones) - 1:
                return True
            
            # Try all possible new step sizes (lastStep-1, lastStep, lastStep+1)
            for new_steps in [lastStep - 1, lastStep, lastStep + 1]:
                if stones[curr_idx] + new_steps in indices and indices[stones[curr_idx] + new_steps] > curr_idx:
                    # If the frog can jump to the new stone and continue the path, return True
                    if dfs(new_steps, indices[stones[curr_idx] + new_steps]):
                        dp[(lastStep, curr_idx)] = True
                        return True
                
            # If no valid path can be found, return False
            dp[(lastStep, curr_idx)] = False
            return False
        
        # Start the DFS traversal from the first stone with an initial jump size of 1
        return dfs(1, 1)



print(Solution().canCross([0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]))

