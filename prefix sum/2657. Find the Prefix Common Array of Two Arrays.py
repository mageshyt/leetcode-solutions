"""

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

 

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
Example 2:

Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

"""
from typing import List
from collections import defaultdict

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hash1=defaultdict(int)
        hash2=defaultdict(int)

        res=[0]*len(A)

        if A[0]==B[0]:
            res[0]=1
        hash1[A[0]]=1
        hash2[B[0]]=1
        

        for i in range(1,len(A)):
            currA,currB=A[i],B[i]
            hash1[currA]+=1
            hash2[currB]+=1

            # case 1 if both are in hash1 and hash2
            if currA in hash2 and currB in hash1:
                if currA == currB:
                    res[i]=res[i-1]+1
                else:
                    res[i]=res[i-1]+2

            elif currA in hash2 and currB not in hash1:
                res[i]=res[i-1] + 1

            elif currA not in hash2 and currB in hash1:
                res[i]=res[i-1] + 1

            else:
                res[i]=res[i-1]

        return res

s=Solution()
print(s.findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))
print(s.findThePrefixCommonArray([2,3,1],[3,1,2]))
