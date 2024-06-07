"""In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
"""

from typing import List
from collections import defaultdict
class Solution:
    # Time : (n*m) n is the number of words in the sentence and m is the number of words in the dictionary
    # Space : O(n) n is the number of words in the dictionary
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_lengths = defaultdict(int)  # root: length of root

        result = []
        for root in dictionary:
            root_lengths[root] = len(root)

        for word in sentence.split(" "):
            for root in sorted(root_lengths, key=root_lengths.get):
                if word.startswith(root):
                    result.append(root)
                    break
            else:
                result.append(word)

        return " ".join(result)

sentence = "the cattle was rattled by the battery"
dictionary = ["cat","bat","rat"]
print(Solution().replaceWords(dictionary,sentence))
        