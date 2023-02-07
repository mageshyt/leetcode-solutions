'''In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).'''


class Solution:
    def isAlienSorted(self, words, order: str) -> bool:

        order_list = {order[i]: i for i in range(len(order))}

        def helper(word1, word2):
            # check if word1 is lexicographically smaller than word2
            if len(word1) > len(word2):
                return False

            for i in range(min(len(word1), len(word2))):
                if order_list[word1[i]] < order_list[word2[i]]:
                    return True
                elif order_list[word1[i]] > order_list[word2[i]]:
                    return False

                    
            # if same prefix, check length
            return True if len(word1) < len(word2) else False
        for i in range(len(words)-1):
            # if same word , continue
            if words[i] == words[i+1]:
                continue
            if not helper(words[i], words[i+1]):
                return False

        return True


if __name__ == "__main__":
    print(Solution().isAlienSorted(
        ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(Solution().isAlienSorted(
        ["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
    print(Solution().isAlienSorted(
        ["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
