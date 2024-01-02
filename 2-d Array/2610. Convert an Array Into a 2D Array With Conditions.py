"""2610. Convert an Array Into a 2D Array With Conditions

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

 

Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array."""


from typing import List
from collections import Counter,defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter=Counter(nums)
        # get max value
        max_val=max(counter.values())
        res=[[] for _ in range(max_val)]

        # iterate over counter
        for key, val in counter.items():
            for i in range(val):
                res[i].append(key)

        return res
    
    def findMatrix2(self, nums: List[int]) -> List[List[int]]:
        count=defaultdict(int)

        res=[]

        for num in nums:
            row=count[num]
            if len(res) <= row:
                res.append([])

            res[row].append(num)
            count[num] += 1

        return res



    
if __name__ == "__main__":
    nums = [1,3,4,1,2,3,1]
    print(Solution().findMatrix2(nums))
