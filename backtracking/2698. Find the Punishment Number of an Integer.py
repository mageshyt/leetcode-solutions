"""
Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

1 <= i <= n
The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
 

Example 1:

Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182
Example 2:

Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
"""
class Solution:
    # time: O(n)
    def punishmentNumber(self, n: int) -> int:
        samples= [1,9,10,36,45,55,82,91,99,100,235,297,369,370,379,414,
               657,675,703,756,792,909,918,945,964,990,991,999,1000]

        # find the punishment number of n
        total = 0

        for num in samples:
            if num <= n:
                total += num*num
            else:
                break
        return total

    def punishmentNumber(self, n: int) -> int:

        def backtrack(s:str,target:int)->bool:
            # GOAL
            if s=="" and target==0:
                return True


            # CONSTRAINT
            if target<0:
                return False

            # CHOICE
            for i in range(len(s)):
                left=s[:i+1] # left is the left part of the string
                right=s[i+1:] # right is the right part of the string
                if backtrack(right,target-int(left)):
                    return True

            return False


        total=0

        for i in range(1,n+1):
            square=i*i

            if backtrack(str(square),i):
                total+=square

        return total

            

s=Solution()

print(s.punishmentNumber(10)) # 182
print(s.punishmentNumber(37)) # 1478

