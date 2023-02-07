"""You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
"""
import collections


class Solution:
    def totalFruit(self, fruits) -> int:
        window_start = 0

        max_length = 0

        # fequency map
        fruit_frequency = collections.defaultdict(int)

        for window_end in range(len(fruits)):
            right_fruit = fruits[window_end]
            fruit_frequency[right_fruit] += 1

            # when we have 3 types of fruits in the window
            while len(fruit_frequency) > 2:
                left_fruit = fruits[window_start]
                # decrement the frequency of the fruit going out of the window
                # move the window to the right
                fruit_frequency[left_fruit] -= 1
                if fruit_frequency[left_fruit] == 0:
                    del fruit_frequency[left_fruit]  # shrink the window

                window_start += 1  # shrink the window

            max_length = max(max_length, window_end - window_start + 1)

        return max_length


if __name__ == "__main__":
    print(Solution().totalFruit([1, 2, 1]))
