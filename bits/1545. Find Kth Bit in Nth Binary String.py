"""
Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".
 

Constraints:

1 <= n <= 20
"""
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.dfs(n, k)

    def dfs(self, n, k):
        # base case
        if n==1:
            return "0"
        
        # find the length of the string
        length = 2**n - 1
        
        # find the middle index
        mid = length // 2 + 1
        
        if k==mid:
            return "1"
        
        if k < mid:
            return self.dfs(n-1, k)
        
        # k > mid
        # find the mirror index
        mirror = length - k + 1
        
        # invert and reverse the string
        return self.invert(self.reverse(self.dfs(n-1, mirror)))


    def invert(self, s):
        # invert all the bits in s
        return "".join(["1" if c=="0" else "0" for c in s])

    def reverse(self, s):
        return s[::-1]


# Time complexity: O(2^n)
# Space complexity: O(2^n)

print(Solution().findKthBit(3, 1)) # 0
