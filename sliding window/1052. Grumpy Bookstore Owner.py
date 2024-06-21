"""There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
 

Constraints:

n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1."""
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 1. Calculate the total satisfied customers without using the technique (initial satisfied customers)
        initial_satisfied_customers = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                initial_satisfied_customers += customers[i]

        # 2. Calculate the total satisfied customers using the technique (maximum satisfied customers) 
        n=len(customers)
        # sliding window

        window_start = 0

        # calculate the initial sum of the window

        window_sum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                window_sum += customers[i]

        max_window_sum = window_sum

        for window_end in range(minutes, n):
            # check it the next min the owner is grumpy
            if grumpy[window_end] == 1:
                window_sum += customers[window_end]

            # check if the window_start is grumpy
            if grumpy[window_start] == 1:
                # we decrease the window_sum because we move the window_start
                window_sum -= customers[window_start]

            max_window_sum = max(max_window_sum, window_sum)

            window_start += 1


        return initial_satisfied_customers + max_window_sum
    
    
# Time complexity: O(n)
# Space complexity: O(1)

print(Solution().maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3)) # 16
print(Solution().maxSatisfied([1], [0], 1)) # 1


