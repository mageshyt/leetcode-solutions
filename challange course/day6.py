'''Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

 

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58'''

class Solution:
    def sumOddLengthSubarrays(self, arr) :
        total_val=0
        for subarr in range(1,len(arr)+1,2):
            for start in range(len(arr)):
                if start+subarr<=len(arr):
                    total_val+=sum(arr[start:start+subarr])

        return total_val
test=Solution()
print(test.sumOddLengthSubarrays([1,4,2,5,3]))
