"""
    You are given an integer array nums .
Any positive divisor of a natural number x that is strictly less than x is called a
proper divisor of x. For example, 2 is a proper divisor of 4, while 6 is not a proper
divisor of 6.
You are allowed to perform an operation any number of times on nums, where in each
operation you select any one element from nums and divide it by its greatest proper
divisor.
Return the minimum number of operations required to make the array non-
decreasing.
If it is not possible to make the array non-decreasing using any number of operations,
return -1.
xample 1:

Input: nums = [25,7]

Output: 1

Explanation:

Using a single operation, 25 gets divided by 5 and nums becomes [5, 7].

"""
from typing import List
from math import isqrt

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        
        if all(nums[i] <= nums[i + 1] for i in range(n - 1)):
            return 0
            
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
                
            original = nums[i]
            target = nums[i + 1]
            
            if self.is_prime(original) and original > target:
                return -1
                
            curr_ops = 0
            while nums[i] > target:
                gpd = self.find_largest_divisor(nums[i])
                if gpd == 1:
                    return -1
                nums[i] //= gpd
                curr_ops += 1
                
            operations += curr_ops
            
        return operations
    
    def find_largest_divisor(self, num: int) -> int:
        if num % 2 == 0:
            return num // 2
            
        sqrt = isqrt(num)
        for i in range(3, sqrt + 1, 2):
            if num % i == 0:
                return num // i
                
        for i in range(sqrt, 1, -1):
            if num % i == 0:
                return num // i
        return 1
    
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
            
        for i in range(3, isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True
# Example usage:
sol = Solution()
print(sol.minOperations([25, 7]))  # Output: 1
print(Solution().minOperations([10,25,7])) # 1
print(Solution().minOperations([7,7,6])) # 1
print(Solution().minOperations([1,1,1])) # 1
        
