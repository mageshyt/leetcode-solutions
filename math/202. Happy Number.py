'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1'''


class Solution:
    def isHappy(self, n: int) -> bool:
        sum_of_squares = 0

        hash_set = set() # to store sum of squares

        while sum_of_squares != 1:
            squares = 0

            for i in str(n):
                squares += int(i) ** 2 # square of each digit 


            sum_of_squares = squares

            if sum_of_squares in hash_set:
                return False # if sum of squares is already in hash set, then it is a loop


            hash_set.add(sum_of_squares) # add sum of squares to hash set

            n = sum_of_squares # update n

 
        return True




if __name__ == '__main__':
    n = 2
    print(Solution().isHappy(n))





