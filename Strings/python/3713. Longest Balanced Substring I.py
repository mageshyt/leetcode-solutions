"""
You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

 

Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "zzabccy"

Output: 4

Explanation:

The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​

Example 3:

Input: s = "aba"

Output: 2

Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

"""

from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        max_length = 0
        char_count = defaultdict(int)
        left = 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            while len(set(char_count.values())) > 1:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)


        return max_length


if __name__ == "__main__":
    s = "zzabccy"
    print(Solution().longestBalanced(s))
    print(Solution().longestBalanced("aba"))
    print(Solution().longestBalanced("abbac"))

