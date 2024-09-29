"""
There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone.

Example:

Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum
Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be |10 - 20| + |20 - 10| = 20.
Expected Time Complexity: O(n*k)
Expected Auxilary Space: O(n)

"""
# Type: Array, Dynamic Programming

class Solution:
    def minimizeCost(self, k, arr):
        # recursive function to find the minimum cost
        memo = {}

        def dfs(start):
            # base case
            if start == len(arr) - 1:
                return 0
            if start in memo:
                return memo[start]

            result = float('inf')

            for i in range(1, k + 1):
                if start + i < len(arr):
                    # go upto k steps
                    curr_cost = abs(arr[start] - arr[start + i]) + dfs(start + i)

                    result = min(result, curr_cost)

            memo[start] = result
            return result
        return dfs(0)

print(Solution().minimizeCost(3, [10, 30, 40, 50, 20])) # 30
