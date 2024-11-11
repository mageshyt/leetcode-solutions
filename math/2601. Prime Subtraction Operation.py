"""
You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

 

Example 1:

Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.
"""
from typing import List
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # check if a number is prime
        def is_prime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False


            return True

        primes=[False,False]

        for i in range(2,max(nums)+1):
            if is_prime(i):
                primes.append(True)
            else:
                primes.append(False)

        prev = 0
        for n in nums:
            upper_bound = n - prev # the largest prime number that can be subtracted
            largest_prime = 0
            # find the largest prime number that can be subtracted
            for i in reversed(range(2,upper_bound)):
                if primes[i]:
                    largest_prime = i
                    break

            # its impossible to make the array strictly increasing
            if n- largest_prime <= prev:
                return False

            prev = n - largest_prime


        return True

# Time complexity: O(n*sqrt(n))
# Space complexity: O(1)
print(Solution().primeSubOperation([4,9,6,10])) # True
        
