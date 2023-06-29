import math

"""You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.

Return the total number of beautiful pairs in nums.

Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.

"""


class Solution :
    def countBeautifulPairs(self, nums):
        res=0
        for i in range(len(nums)):
            first=nums[i]

            for j  in range(i+1,len(nums)):

                if math.gcd(first,nums[j])==1:
                    res+=1


        return res

nums=[31,25,72,79,74]

s=Solution()
print(s.countBeautifulPairs(nums))