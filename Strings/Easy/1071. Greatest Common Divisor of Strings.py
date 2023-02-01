"""For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # math solution
        # If str1 + str2 != str2 + str1, then there is no common divisor
        if str1 + str2 != str2 + str1:
            return ""

        return str1[:math.gcd(len(str1), len(str2))]

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # string solution

        len1 = len(str1)
        len2 = len(str2)

        def isDivisor(s):
            # check if s is a divisor of both strings
            if len1 % l or len2 % l:
                return False

            f1 = len1//l
            f2 = len2//l

            return str1[:l]*f1 == str1 and str1[:l]*f2 == str2


        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]

        return ""


if __name__ == "__main__":
    print(Solution().gcdOfStrings("ABCABC", "ABC"))
    print(Solution().gcdOfStrings("ABABAB", "ABAB"))
    print(Solution().gcdOfStrings("LEET", "CODE"))
