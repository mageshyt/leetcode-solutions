"""
You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

Example 1:

Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
Example 2:

Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.

"""

from collections import Counter, defaultdict


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        d1, d2 = defaultdict(int), defaultdict(int)

        for i in range(len(s1)):
            if i % 2 == 0:
                d1[s1[i]] += 1
                d2[s2[i]] += 1
            else:
                d1[s1[i]] -= 1
                d2[s2[i]] -= 1
        return d1 == d2
if __name__ == "__main__":
    print(Solution().checkStrings("abcdba","cabdab"))
