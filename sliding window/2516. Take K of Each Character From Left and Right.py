"""
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        max_allowed_counts = {char: s.count(char) - k for char in 'abc'}
        if any(count < 0 for count in max_allowed_counts.values()):
            return -1

        current_window_counts = {char: 0 for char in 'abc'}
        max_valid_window_size = 0
        left_index = 0

        for right_index, char in enumerate(s):
            current_window_counts[char] += 1
            while current_window_counts[char] > max_allowed_counts[char]:
                current_window_counts[s[left_index]] -= 1
                left_index += 1
            max_valid_window_size = max(max_valid_window_size, right_index - left_index + 1)

        return len(s) - max_valid_window_size

print(Solution().takeCharacters("aabaaaacaabc", 2)) # 8


