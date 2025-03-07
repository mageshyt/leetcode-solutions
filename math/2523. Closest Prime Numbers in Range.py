"""
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 
"""

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        seive=[1]*(right+1)

        seive[0]=0
        seive[1]=0
        for i in range(2,int(right**0.5)+1):
            if seive[i]:
                for j in range(i*i,right+1,i):
                    seive[j]=0
        primes=[]
        for i in range(left,right+1):
            if seive[i]:
                primes.append(i)
        if len(primes)<2:
            return [-1,-1]

        min_diff=float('inf')
        res=[]
        for i in range(1,len(primes)):
            if primes[i]-primes[i-1]<min_diff:
                min_diff=primes[i]-primes[i-1]
                res=[primes[i-1],primes[i]]

        return res


