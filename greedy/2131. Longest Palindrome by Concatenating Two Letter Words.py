"""You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx"."""

import collections


class Solution:
    def longestPalindrome(self, words) -> int:

        word_map = collections.defaultdict(int)

        max_len = 0

        for word in words:
            reverse = self.reverseString(word)

            if word_map[word] > 0:
                # if it is there then decrement the count
                word_map[word] -= 1
                max_len += 4
            else:
                word_map[reverse] += 1  # increment the count of the word
        print(word_map)
        more_palindrome = []

        for word, count in word_map.items():
            # if word is self palindrome
            if word == self.reverseString(word) and count > 0:
                more_palindrome.append(word)

        if len(more_palindrome) > 0:
            max_len += 2  # add 2 for the middle character

        return max_len

    def reverseString(self, s) -> str:

        return s[::-1]

 
if __name__ == "__main__":
    s = Solution()
    # print(s.longestPalindrome(["dd", "aa", "bb", "dd", "aa",
    #       "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"]))

    print(s.longestPalindrome(["cc", "ll", "xx"]))
