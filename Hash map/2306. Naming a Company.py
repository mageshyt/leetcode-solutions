'''You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.

 

Example 1:

Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
Example 2:

Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.'''
import collections


class Solution:
    def distinctNames(self, ideas) -> int:

        distMap = collections.defaultdict(set)

        valid_name = 0

        for idea in ideas:
            first_char = idea[0]
            distMap[first_char].add(idea[1:])

        for [char1, words1] in distMap.items():
            for [char2, words2] in distMap.items():

                # if both have same starting letter
                if char1 == char2:
                    continue

                intersection = 0  # no of duplicate

                for w in words1:
                    # it is a duplicate so increment intersection
                    if w in words2:
                        intersection += 1

                dist_1 = len(words1) - intersection  # no of unique
                dist_2 = len(words2) - intersection  # no of unique

                valid_name += dist_1 * dist_2  # no of valid names 

        return valid_name


ideas = ["coffee", "donuts", "time", "toffee"]
s = Solution()
print(s.distinctNames(ideas))
