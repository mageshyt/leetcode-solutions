"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

The last character of a word is equal to the first character of the next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.


"""
class Solution:
    # O(n) time and O(n) space
    def isCircularSentence(self, sentence: str) -> bool:
        words=sentence.split()
        if len(words)==1:
            return False

        start=words[0][0]

        if words[-1][-1] != start:
            return False

        for i in range(1,len(words)):
            if words[i-1][-1] != words[i][0]:
                return False

        return True
        
