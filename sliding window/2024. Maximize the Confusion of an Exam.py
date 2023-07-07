"""A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

 

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
"""


class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:

        # base case
        if len(s) <= 1:
            return len(s)

        res = 0
        freq = {}
        window_start = 0
        maxRepeatLetterCount = 0

        for windowEnd in range(len(s)):
            curr = s[windowEnd]  # right pointer
            # add the feq
            freq[curr] = freq.get(curr, 0)+1

            # max repeated character
            maxRepeatLetterCount = max(maxRepeatLetterCount, freq[curr])

            while (windowEnd-window_start+1) - maxRepeatLetterCount > k:
                # move our window
                left_char = s[window_start]
                freq[left_char] -= 1
                window_start += 1

            size = windowEnd-window_start+1

            res = max(res, size)

        return res
