from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cache={}
        TEAM_SIZE=3

        def dfs(i, prev, count ):

            if (i, prev, count) in cache:
                return cache[(i, prev, count)]
            # base case
            if count == TEAM_SIZE:
                return 1

            if i == len(rating):
                return 0

            res=0

            for j in range(i, len(rating)):
                pass





# Time complexity: O(N^2)
# Space complexity: O(1)

print(Solution().numTeams([2,5,3,4,1])) # 3