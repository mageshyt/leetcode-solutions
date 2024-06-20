"""In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000."""

from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # sort the position  so that we can apply binary search
        position.sort()

        # base case
        if m == 2:
            return position[-1] - position[0]
        
        # binary search
        # since the min dist can't be less then 1 and max distance can be the distance between the first and last basket
        low ,high=1,position[-1]-position[0] 

        # helper function to tell how much ball we can put in the basket with the given distance

        def is_possible(distance):
            count=1
            last_position=position[0]
            for i in range(1,len(position)):
                if position[i]-last_position>=distance:
                    count+=1
                    last_position=position[i]

            return count>=m
        
        while low<high:
            mid=(low+high)//2
            if is_possible(mid):
                low=mid+1
            else:
                high=mid

        return low-1
    
# test the solution

print(Solution().maxDistance([1,2,3,4,7],3)) # 3
print(Solution().maxDistance([5,4,3,2,1,1000000000],2)) # 999999999
print(Solution().maxDistance([79,74,57,22],4)) # 2


