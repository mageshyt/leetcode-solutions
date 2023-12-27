"""2974. Minimum Number Game"""
from typing import List
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        empty = [0] * len(nums)
        move1=1
        move2=0

        nums.sort()

        for idx,num in enumerate(nums):
            if idx%2==0:
                empty[move1]=num
                move1+=2
            else:
                empty[move2]=num
                move2+=2

 
        return empty

print(Solution().numberGame([5,4,2,3]))
        
"""2975. Maximum Square Area by Removing Fences From a Field"""