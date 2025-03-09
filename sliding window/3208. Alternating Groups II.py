"""

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3
"""

from typing import List
class Solution:
    # Time: O(n) | Space: O(1)
    def alternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        count=0
        left=0

        for right in range(n):
            if right > 0 and colors[right%n]==colors[right-1]:
                left=right
            # if we have k alternating colors
            if right-left+1==k:
                count+=1
                left+=1

        return count

print(Solution().alternatingGroups([0,1,0,1,0],3)) #2
print(Solution().alternatingGroups([0,1,0,1,0],4)) #1
