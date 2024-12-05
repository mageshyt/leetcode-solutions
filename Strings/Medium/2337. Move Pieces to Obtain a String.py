"""
    You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

 

Example 1:

Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.
"""

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        p1, p2 = 0, 0

        while p1 < n or p2<n :

            # move p1 and p2 to the next piece
            while p1 < n and start[p1] == '_':
                p1 += 1
            while p2 < n and target[p2] == '_':
                p2 += 1


            if p1 == n and p2 == n:
                return True

            # if one of the strings has ended, return False
            if p1 == n or p2 == n:
                return False

            # if the pieces are different, return False
            if start[p1] != target[p2]:
                return False


            # if the piece is 'L', it can only move to the left
            if start[p1] == 'L' and p1 < p2:
                return False
            
            # if the piece is 'R', it can only move to the right
            if start[p1] == 'R' and p1 > p2:
                return False


            p1 += 1
            p2 += 1

        return True

s = Solution()
print(s.canChange("_L__R__R_", "L______RR"))


