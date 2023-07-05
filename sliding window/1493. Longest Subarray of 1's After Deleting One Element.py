from typing import List
 
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window_start=0


        res=0


        zero_count=0  
        
        for window_end in range(0,len(nums)):
            curr=nums[window_end] 

            zero_count+=(curr==0)

            while zero_count >1:

                zero_count-=(nums[window_start] ==0 )

                window_start+=1

            res=max(res,window_end-window_start)
             

        return res 


nums = [1,1,0,0,1,1,1,0,1]

print(Solution().longestSubarray(nums))
            




