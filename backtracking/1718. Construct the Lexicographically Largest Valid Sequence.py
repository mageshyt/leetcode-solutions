"""

Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

"""
from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res=[0]*(2*n-1)
        visited=set()

        def backtrack(i):
            if i==2*n-1:
                return True
            if res[i]:
                return backtrack(i+1)
            for num in range(n,0,-1):
                if num in visited:
                    continue
                if num==1:
                    res[i]=1
                    visited.add(1)
                    if backtrack(i+1):
                        return True
                    res[i]=0
                    visited.remove(1)
                elif i+num<2*n-1 and not res[i+num]:
                    res[i]=num
                    res[i+num]=num
                    visited.add(num)
                    if backtrack(i+1):
                        return True
                    res[i]=0
                    res[i+num]=0
                    visited.remove(num)
            return False


        backtrack(0)


        return res


s=Solution()

print(s.constructDistancedSequence(5)) # [5,3,1,4,3,5,2,4,2]
