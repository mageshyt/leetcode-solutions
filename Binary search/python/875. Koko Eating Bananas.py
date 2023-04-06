'''Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23'''


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2

            if self.canFinish(piles, k, h):
                right = k - 1
            else:
                left = k + 1

        return left

    def canFinish(self, piles, speed, h):
        time = 0
        for pile in piles:
            time += pile // speed
            if pile % speed != 0:
                time += 1

        return time <= h


if __name__ == "__main__":
    s = Solution()
    piles = [30, 11, 23, 4, 20]
    h = 6
    print(s.minEatingSpeed(piles, h))