#User function Template for python3
"""
Given an array arr of size n of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

Note: Answer can be very large, so, output answer modulo 109+7.

Examples:

Input: 
n = 6, arr = [5, 2, 3, 10, 6, 8], sum = 10
Output: 
3
Explanation: 
{5, 2, 3}, {2, 8}, {10} are possible subsets.
Input: 
n = 5, arr = [2, 5, 1, 4, 3], sum = 10
Output: 
3
Explanation: 
{2, 1, 4, 3}, {5, 1, 4}, {2, 5, 3} are possible subsets.

"""
class Solution:
    def perfectSum(self, numbers, length, targetSum):
        dp = [1] + [0] * targetSum
        print(dp)

        MOD = 10**9 + 7 

        for number in numbers:
            for currentSum in range(targetSum, number - 1, -1):
                dp[currentSum] = (dp[currentSum] + dp[currentSum - number]) % MOD
        
        return dp[targetSum]

print(Solution().perfectSum([2,3,5,6,8,10],6,10)) # 3
		
