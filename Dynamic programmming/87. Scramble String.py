"""We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true."""


class Solution:

    def __init__(self) -> None:
        self.memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # base case

        if (s1 == s2):
            return True

        if (n == 1):
            return False

        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]

        # split the string into two parts

        for i in range(1, n):

            # 1 . s1[:i] and s2[:j] are scrambled and s1[i:] and s2[j:] are scrambled

            # s1 left part and s2 left part are scrambled
            # s1 right part and s2 right part are scrambled
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])):
                self.memo[(s1, s2)] = True
                return True

            # 2. s1[:i] and s2[-j:] are scrambled and s1[i:] and s2[:-j] are scrambled

            # s1 left part and s2 right part are scrambled
            # s1 right part and s2 left part are scrambled
            if (self.isScramble(s1[:i], s2[n-1:]) and self.isScramble(s1[i], s2[:n-i])):
                self.memo[(s1, s2)] = True
                return True

        self.memo[(s1, s2)] = False
        return False


if __name__ == "__main__":
    s1 = "great"
    s2 = "rgeat"
    print(Solution().isScramble(s1, s2))
