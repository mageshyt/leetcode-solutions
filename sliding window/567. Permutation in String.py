'''Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false'''

import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False

        s1_count = [0]*26  # count of each character in s1
        s2_count = [0]*26  # count of each character in s2

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s1), len(s2)):

            if s1_count == s2_count:
                return True

            curr = s2[i]  # current character
            prev = s2[i-len(s1)]  # previous character
            print(curr, prev)

            s2_count[ord(curr) - ord('a')] += 1  # add the current character
            # remove the previous character
            s2_count[ord(prev) - ord('a')] -= 1

        return s1_count == s2_count


if __name__ == "__main__":

    s = Solution()
    # print(s.checkInclusion("a", "ab"))
    print(s.checkInclusion("ab", "eidboaboo"))
