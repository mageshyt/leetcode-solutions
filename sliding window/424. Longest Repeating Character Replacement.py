'''You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABB'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        windowStart = 0
        maxLength = 0

        frequencyMap = {}  # char: count
        maxRepeatLetterCount = 0
        for windowEnd in range(len(s)):

            rightChar = s[windowEnd]  # current char

            frequencyMap[rightChar] = frequencyMap.get(
                rightChar, 0)+1  # update the freq

            maxRepeatLetterCount = max(
                maxRepeatLetterCount,  frequencyMap[rightChar])

            # window_length = windowEnd - windowStart + 1  # to get window size

            while (windowEnd - windowStart + 1) - maxRepeatLetterCount > k:
                leftChar = s[windowStart]
                frequencyMap[leftChar] -= 1
                windowStart += 1

            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement("ABAB", 2))
