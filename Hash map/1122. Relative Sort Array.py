
from typing import List
from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # create a dictionary to store the frequency of each element in arr1
        freq=defaultdict(int)
        for i in arr1:
            freq[i]+=1

        # create a list to store the elements in arr1 that are in arr2
        result=[]
        for i in arr2:
            result+=[i]*freq[i]
            freq.pop(i)

        # sort the remaining elements in arr1
        for i in sorted(freq.keys()):
            result+=[i]*freq[i]

        return result




# Time complexity: O(nlogn)
# Space complexity: O(n)

print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))
