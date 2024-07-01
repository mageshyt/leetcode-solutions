"""Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.


Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds"""

from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(0,len(arr)-2):
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
                return True

        return False

# Time complexity: O(n)
# Space complexity: O(1)
print(Solution().threeConsecutiveOdds([2,6,4,1])) # False
print(Solution().threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])) # True
