"""
ven a strings and an integer k, return the total number of substrings of s where at
ast one character appears at least k times.
substring is a contiguous non-empty sequence of characters within a string.
"""
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        char_count = defaultdict(int)
        left = 0
        valid_substring_count = 0

        for right in range(n):
            char_count[s[right]] += 1

            # When any character's count becomes >= k, start counting valid substrings
            while any(count >= k for count in char_count.values()):
                valid_substring_count += n - right  # All substrings from left to right are valid
                char_count[s[left]] -= 1  # Shrink the window by moving left pointer
                left += 1

        return valid_substring_count

print(Solution().numberOfSubstrings("abacb", 2)) # 10

print(Solution().numberOfSubstrings("abcde", 1)) # 10



