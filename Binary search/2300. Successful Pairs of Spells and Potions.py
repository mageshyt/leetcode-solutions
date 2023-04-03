"""ou are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned."""


class Solution:
    def successfulPairs(self, spells, potions, success: int):

        res = []

        # 1. sort the potions
        potions.sort()  # O(nlogn)

        for spell in spells:

            # to find the potion that is greater than the (spell*potion) >= success
            idx = len(potions)

            l = 0
            r = len(potions)-1

            while l <= r:

                mid = (l+r)//2

                if spell*potions[mid] >= success:
                    idx = mid
                    r = mid-1
                else:
                    l = mid+1

            res.append(len(potions)-idx)

        return res


if __name__ == "__main__":
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7

    print(Solution().successfulPairs(spells, potions, success))
