"""You are given a 0-indexed integer array nums, and an integer k.

The K-or of nums is a non-negative integer that satisfies the following:

The ith bit is set in the K-or if and only if there are at least k elements of nums in which bit i is set.
Return the K-or of nums.

Note that a bit i is set in x if (2i AND x) == 2i, where AND is the bitwise AND operator.

 

Example 1:

Input: nums = [7,12,9,8,9,15], k = 4
Output: 9
Explanation: Bit 0 is set at nums[0], nums[2], nums[4], and nums[5].
Bit 1 is set at nums[0], and nums[5].
Bit 2 is set at nums[0], nums[1], and nums[5].
Bit 3 is set at nums[1], nums[2], nums[3], nums[4], and nums[5].
Only bits 0 and 3 are set in at least k elements of the array, and bits i >= 4 are not set in any of the array's elements. Hence, the answer is 2^0 + 2^3 = 9.
Example 2:

Input: nums = [2,12,1,11,4,5], k = 6
Output: 0
Explanation: Since k == 6 == nums.length, the 6-or of the array is equal to the bitwise AND of all its elements. Hence, the answer is 2 AND 12 AND 1 AND 11 AND 4 AND 5 = 0.
Example 3:

Input: nums = [10,8,5,9,11,6,8], k = 1
Output: 15
Explanation: Since k == 1, the 1-or of the array is equal to the bitwise OR of all its elements. Hence, the answer is 10 OR 8 OR 5 OR 9 OR 11 OR 6 OR 8 = 15.
 """

from typing import List
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        # 1. find the max number in the array
        max_num = max(nums)
        # 2. find the number of bits in the max number
        max_bits = len(bin(max_num))-2
        # 3. iterate over the bits and find the number of elements in the array whose bit is set
        # 4. if the number of elements is greater than or equal to k, then set the bit in the answer
        # 5. return the answer
        ans = 0
        for i in range(max_bits):
            count = 0
            for num in nums:
                if num & (1<<i):
                    count += 1
            if count >= k:
                ans |= (1<<i)
        return ans
        
        


if __name__ == "__main__":
    nums = [7,12,9,8,9,15]
    k = 4
    print(Solution().findKOr(nums,k))
    
"""
You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.

 

Example 1:

Input: nums1 = [3,2,0,1,0], nums2 = [6,5,0]
Output: 12
Explanation: We can replace 0's in the following way:
- Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.
Example 2:

Input: nums1 = [2,0,2,0], nums2 = [1,4]
Output: -1
Explanation: It is impossible to make the sum of both arrays equal.
"""



class Solution:
    def minOperations(self, nums1, nums2):
        sum1, sum2 = sum(nums1), sum(nums2)
        zeros1, zeros2 = nums1.count(0), nums2.count(0)
        
        if sum1 > sum2:
            sum1, sum2, zeros1, zeros2 = sum2, sum1, zeros2, zeros1
        
        diff = abs(sum1 - sum2)
        
        if diff == 0:
            return 0
        
        if diff % 2 == 0:
            if zeros1 >= diff // 2:
                return diff // 2
            else:
                return zeros1 + zeros2 - diff // 2
        else:
            return -1

# Example usage
if __name__ == "__main__":
    nums1 = [3, 2, 0, 1, 0]
    nums2 = [6, 5, 0]
    solution = Solution()
    result = solution.minOperations(nums1, nums2)
    print(result)  # Output: 12




"""There exists an undirected tree rooted at node 0 with n nodes labeled from 0 to n - 1. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given a 0-indexed array coins of size n where coins[i] indicates the number of coins in the vertex i, and an integer k.

Starting from the root, you have to collect all the coins such that the coins at a node can only be collected if the coins of its ancestors have been already collected.

Coins at nodei can be collected in one of the following ways:

Collect all the coins, but you will get coins[i] - k points. If coins[i] - k is negative then you will lose abs(coins[i] - k) points.
Collect all the coins, but you will get floor(coins[i] / 2) points. If this way is used, then for all the nodej present in the subtree of nodei, coins[j] will get reduced to floor(coins[j] / 2).
Return the maximum points you can get after collecting the coins from all the tree nodes.

 

Example 1:


Input: edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5
Output: 11                        
Explanation: 
Collect all the coins from node 0 using the first way. Total points = 10 - 5 = 5.
Collect all the coins from node 1 using the first way. Total points = 5 + (10 - 5) = 10.
Collect all the coins from node 2 using the second way so coins left at node 3 will be floor(3 / 2) = 1. Total points = 10 + floor(3 / 2) = 11.
Collect all the coins from node 3 using the second way. Total points = 11 + floor(1 / 2) = 11.
It can be shown that the maximum points we can get after collecting coins from all the nodes is 11. 
"""

class Solution:
    def maximumPoints(self, edges, coins, k):
        graph = [[] for _ in range(len(coins))] 
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        dp={}
        
        def dfs(node, parent, coins,way=1):
            # base case
            if node == None:
                return 0

            if len(graph[node]) == 1 and graph[node][0] == parent:
                return coins[node]
            

            if (node, parent, way) in dp:
                return dp[(node, parent, way)]
            # logic

            max_points = (coins[node] - k) if way == 1 else (coins[node] // 2)

            # if way 2 then subtree of node coin will be reduced to half
            modified_coins = coins.copy()
            if way == 2:
                for child in graph[node]:
                    if child != parent:
                        modified_coins[child] = modified_coins[child] // 2
   
            for child in graph[node]:
                if child != parent:
                    max_points += max(dfs(child, node, modified_coins,1), dfs(child, node, modified_coins,2))

            dp[(node, parent, way)] = max_points

            return max_points
        
        return dfs(0, None, coins,1)

if __name__ == "__main__":
    print("--------")
    edges = [[0,1],[2,0],[0,3],[4,2]]
    coins = [7,5,0,9,3]
    k = 4
    solution = Solution()
    result = solution.maximumPoints(edges, coins, k)
    print(result)
