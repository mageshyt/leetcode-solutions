'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 '''
from collections import Counter


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        # if both pattern and words have same length
        if len(pattern) != len(words):
            return False
        # if both pattern and words have same unique length
        if len(set(pattern)) != len(set(words)):
            return False

        hash_map = {}

        for i in range(len(pattern)):
            if pattern[i] not in hash_map:
                hash_map[pattern[i]] = words[i]
            else:
                if hash_map[pattern[i]] != words[i]:
                    return False

        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))
