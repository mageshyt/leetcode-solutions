"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
"""

from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds=0
        for i in range(0,len(arr)):
            if arr[i] & 1:
                odds+=1
            else:
                odds=0

            if odds==3:
                return True

        return False
