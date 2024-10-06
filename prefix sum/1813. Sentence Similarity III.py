"""
You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

For example,

s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"

Output: false

Explanation:

No single sentence can be inserted inside one of the sentences to make it equal to the other.


"""
from collections import deque 
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # split the sentences into words
        deque1= deque(sentence1.split())
        deque2 = deque(sentence2.split())


        # remove the common words from the beginning and the end of the sentences

        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.popleft()
            deque2.popleft()

        # remove the common words from the end of the sentences

        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop()
            deque2.pop()

        # check if the two sentences are similar
        return not deque1 or not deque2

# Time complexity: O(n)
# Space complexity: O(n)

print(Solution().areSentencesSimilar("My name is Haley", "My Haley")) # True
print(Solution().areSentencesSimilar("of", "A lot of words")) # False
print(Solution().areSentencesSimilar("Hello Jane", "Hello my name is Jane")) # True
print(Solution().areSentencesSimilar("Frog cool", "Frogs are cool")) # False
print(Solution().areSentencesSimilar("Eating right now", "Eating")) # True
