"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 """


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        left = 0
        right = len(haystack)-1
        s = ""
        while left <= right:
            if haystack[left] == needle[0]:

                p1 = left

                while p1 < len(haystack) and p1 < left+len(needle):
                    s += haystack[p1]
                    p1 += 1

                if s == needle:
                    return left
                else:
                    s = ""
            left += 1
        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"

    print(Solution().strStr(haystack, needle))
