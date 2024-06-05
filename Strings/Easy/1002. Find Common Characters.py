"""
Given a string array words, return an array of all characters that show up in all strings within
the words (including duplicates). You may return the answer in any order.



Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

"""

from typing import List
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        prevCounter= Counter(words[0])
        for word in words[1:]:
            currentCounter= Counter(word)
            for key in prevCounter:
                prevCounter[key]= min(prevCounter[key], currentCounter[key])
        result= []
        for key in prevCounter:
            result+= [key]*prevCounter[key]

        return result



print(Solution().commonChars(["bella","label","roller"])) # ["e","l","l"]
print(Solution().commonChars(["cool","lock","cook"])) # ["c","o"]
