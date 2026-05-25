"""
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false

"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] != '0':
            return False
        
        reachable = [False] * n
        reachable[0] = True
        count = 0
        
        for i in range(minJump, n):
            count += 1 if reachable[i - minJump] else 0
            
            if i > maxJump:
                count -= 1 if reachable[i - maxJump - 1] else 0
            
            reachable[i] = count > 0 and s[i] == '0'
        
        return reachable[-1]



