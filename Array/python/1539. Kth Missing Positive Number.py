"""Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9."""


class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        l = 0
        r = len(arr)-1

        while l <= r:
            mid = (l+r)//2
            if arr[mid] - mid - 1 < k: 
                # if the number of missing numbers before arr[mid] is less than k, then we need to search in the right half
                l = mid + 1
            else:
                # if the number of missing numbers before arr[mid] is greater than k, then we need to search in the left half
                r = mid - 1

        return l + k # the number of missing numbers before l is k, so the kth missing number is l+k


arr = [2, 3, 4, 7, 9, 11]
k = 5
print(Solution().findKthPositive(arr, k))
