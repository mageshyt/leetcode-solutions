
from typing import List
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # dictionary to store the frequency of each number
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1

        result=[]
        for key in freq:
            # if the frequency of the number is 1, then add it to the result
            if freq[key]==1:
                result.append(key)

        return result
