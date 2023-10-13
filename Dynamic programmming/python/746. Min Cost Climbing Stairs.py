from typing import List
class Solution:
    def minCostClimbingStairs(self, points: List[int]) -> int:

        cache={}
        n=len(points)

        def dp(step):

            if step >= n:
                return 0
            
            if step in cache:
                return cache[step]
            

            # take 1 step or 2 step

            cache[step]=points[step] + min(dp(step+1),dp(step+2))


            return cache[step]
        
        return min(dp(0),dp(1))

