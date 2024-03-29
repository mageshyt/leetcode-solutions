"""You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:

        if n == 0:
            return True

        # add 0 at the beginning and end of the flowerbed
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            # approach
            # if previous and next are 0, then we can plant a flower

            prev, next = flowerbed[i-1], flowerbed[i+1]

            if prev == 0 and next == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1  # plant a flower
                n -= 1

            if n == 0:
                return True

        return False
