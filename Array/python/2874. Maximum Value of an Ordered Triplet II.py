
from typing import List
class Solution:

        def maximumTripletValue(self, nums: List[int]) -> int:
                
                res=0
                max_left=0
                max_right=0
                for num in nums:
                        res= max(res, num*max_right)
                        max_right=max(max_right,max_left-num)
                        max_left=max(max_left,num)

                return res
        

