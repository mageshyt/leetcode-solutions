from typing import List
from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1

        freq=sorted(freq.items(),key=lambda x:x[1],reverse=True )

        max_freq=freq[0][1]
        max_freq_elements=[ max


sol=Solution()
print(sol.maxFrequencyElements([1,2,2,3,1,4]))