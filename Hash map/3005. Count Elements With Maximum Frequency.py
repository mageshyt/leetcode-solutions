from typing import List
from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1

        freq=sorted(freq.items(),key=lambda x:x[1],reverse=True )

        max_freq=freq[0][1]
        max_freq_elements=0
        print(freq)
        for i in range(len(freq)):
            if freq[i][1]==max_freq:
                max_freq_elements+=max_freq
            else:
                break
        
        return max_freq_elements




sol=Solution()
print(sol.maxFrequencyElements([1,2,2,3,1,4]))