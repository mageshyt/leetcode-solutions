"""6354. Find the Array Concatenation Value
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
You are given a 0-indexed integer array nums.

The concatenation of two numbers is the number formed by concatenating their numerals.

For example, the concatenation of 15, 49 is 1549.
The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:

If there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
If one element exists, add its value to the concatenation value of nums, then delete it.
Return the concatenation value of the nums.



Example 1:

Input: nums = [7,52,2,4]
Output: 596
Explanation: Before performing any operation, nums is [7,52,2,4] and concatenation value is 0.
 - In the first operation:
We pick the first element, 7, and the last element, 4.
Their concatenation is 74, and we add it to the concatenation value, so it becomes equal to 74.
Then we delete them from nums, so nums becomes equal to [52,2].
 - In the second operation:
We pick the first element, 52, and the last element, 2.
Their concatenation is 522, and we add it to the concatenation value, so it becomes equal to 596.
Then we delete them from the nums, so nums becomes empty.
Since the concatenation value is 596 so the answer is 596."""


from collections import defaultdict
import collections


class Solution:
    def findTheArrayConcVal(self, nums):
        ans = 0

        while len(nums) > 1:
            ans += int(str(nums[0])+str(nums[-1]))
            nums.pop(0)
            nums.pop(-1)

        if nums:
            ans += nums[0]

        return ans


"""Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper


Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3)."""


class Solution:
    def countFairPairs(self, nums, lower: int, upper: int) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        ans = 0
        for i in count:
            for j in count:
                if lower <= i + j <= upper:
                    ans += count[i] * count[j]
        return ans


S = Solution()

print(S.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))


"""
User Accepted:7
User Tried:38
Total Accepted:7
Total Submissions:63
Difficulty:Hard
You are given two strings s and t.

You are allowed to remove any number of characters from the string t.

The score string is 0 if no characters are removed from the string t, otherwise:

Let left be the minimum index among all removed characters.
Let right be the maximum index among all removed characters.
Then the score of the string is right - left + 1.

Return the minimum possible score to make t a subsequence of s.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abacaba", t = "bzaa"
Output: 1
Explanation: In this example, we remove the character "z" at index 1 (0-indexed).
The string t becomes "baa" which is a subsequence of the string "abacaba" and the score is 1 - 1 + 1 = 1.
It can be proven that 1 is the minimum score that we can achieve.
Example 2:

Input: s = "cde", t = "xyz"
Output: 3
Explanation: In this example, we remove characters "x", "y" and "z" at indices 0, 1, and 2 (0-indexed).
The string t becomes "" which is a subsequence of the string "cde" and the score is 2 - 0 + 1 = 3.
It can be proven that 3 is the minimum score that we can achieve."""


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        left = 0
        right = 0
        score = 0

        for char in t:
            found = False
            for i in range(right, len(s)):
                if s[i] == char:
                    found = True
                    right = i + 1
                    break

            if not found:
                left += 1
                score = max(score, right - left + 1)

        return score


S = Solution()
print(S.minimumScore("abecdebe", "eaebceae"))
