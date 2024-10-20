"""
You are given a string target.

Alice is going to type target on her computer using a special keyboard that has only two keys:

Key 1 appends the character "a" to the string on the screen.
Key 2 changes the last character of the string on the screen to its next character in the English alphabet. For example, "c" changes to "d" and "z" changes to "a".
Note that initially there is an empty string "" on the screen, so she can only press key 1.

Return a list of all strings that appear on the screen as Alice types target, in the order they appear, using the minimum key presses.



Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""

from typing import List
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res=[]
        if target[0] == 'a':
            res.append('a')

        left= 1 if target[0] == 'a' else 0
        while True:
            if left >= len(target):
                break
            currTarget=target[left]

            if currTarget == 'a':
                if not res:
                    res.append('a')
                else:
                    res.append(res[-1]+'a')
                left+=1

            else:
                # if not then add a and make it untill it is equal to currTarget
                if not res:
                    res.append('a')
                else:
                    res.append(res[-1]+'a')

                while res[-1][-1] != currTarget:
                    a=res[-1][:-1]+chr(ord(res[-1][-1])+1)
                    res.append(a)

                left+=1




        return res



print(Solution().stringSequence(("he")))

        
