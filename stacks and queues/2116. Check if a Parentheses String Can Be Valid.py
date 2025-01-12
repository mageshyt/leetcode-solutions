"""

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

 

Example 1:


Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
 

"""

from typing import List

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        lockedStack=[]
        unLockedStack=[] # have to keep track of unlocked stack

        for i in range(len(s)):
            if locked[i]=="0":
                unLockedStack.append(i)

            elif s[i] == "(":
                lockedStack.append(i)

            else:
                if lockedStack:
                    lockedStack.pop()
                elif unLockedStack:
                    unLockedStack.pop()
                else:
                    return False

        while lockedStack and unLockedStack and lockedStack[-1] < unLockedStack[-1]:
            lockedStack.pop()
            unLockedStack.pop()

        if lockedStack:
            return False

        return len(unLockedStack) % 2 == 0


    # space optimized solution

    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        locked_cnt=0
        unLocked_cnt=0


        for i in range(len(s)):
            if locked[i]=="0":
                unLocked_cnt+=1

            elif s[i] == "(":
                locked_cnt+=1

            else:
                if locked_cnt:
                    locked_cnt-=1
                elif unLocked_cnt:
                    unLocked_cnt-=1
                else:
                    return False

        if locked_cnt == 0:
            return True

        # going from right to left
        locked_cnt=0
        unLocked_cnt=0
        # matching ( 
        for i in reversed(range(len(s))):
            if locked[i]=="0":
                unLocked_cnt+=1

            elif s[i] == ")":
                locked_cnt+=1

            else:
                if locked_cnt:
                    locked_cnt-=1
                elif unLocked_cnt:
                    unLocked_cnt-=1
                else:
                    return False

        return locked_cnt == 0
s = "))()))"
locked = "010100"
print(Solution().canBeValid(s, locked))

s = "()()"
locked = "0000"
print(Solution().canBeValid(s, locked))

s = ")"
locked = "0"
print(Solution().canBeValid(s, locked))


