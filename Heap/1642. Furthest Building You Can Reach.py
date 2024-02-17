"""You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

 

Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
"""
from typing import List
from heapq import heapify
import heapq

class Solution:
    # Time complexity: O(nlogn) | Space complexity: O(n)
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_h=[] # min heap

        for i in range(1,len(heights)):
            jump=heights[i]-heights[i-1] # jump is the difference between the current building and the previous building
            print("[JUMP, BRICKS, LADDERS,MIN_H]: ",jump,bricks,ladders,min_h)
            if jump < 0: continue # if the jump is negative, we don't need to use bricks or ladders

            if jump > 0:
                heapq.heappush(min_h,jump) # if the jump is positive, we need to use bricks or ladders, so we add it to the heap

            if len(min_h) > ladders: # if we have more jumps than ladders, we need to use bricks
                bricks -= heapq.heappop(min_h) # we use the needed bricks

            if bricks < 0: # if we don't have any bricks left, we can't go further
                return i-1
            
        return len(heights)-1 # if we have enough bricks to go through all the buildings, we return the last building
    
            





if __name__ == "__main__":
    print(Solution().furthestBuilding([4,2,7,6,9,14,12],5,1))
