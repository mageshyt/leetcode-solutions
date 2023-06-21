"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
 """


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float('inf')] * (len(word2)+1) for i in range(len(word1)+1)]
        # first mark no of operation for base cases

        # 1. last rows
        for j in range(len(word2)+1):
            # when word 1 is not empty
            cache[len(word1)][j] = len(word2)-j

        # last column
        for i in range(len(word1)+1):
            # when word 2    is not empty
            cache[i][len(word2)] = len(word1)-i

        # insert -> (i , j+1)
        # delete -> (i+1,j)
        # replace -> (i+1,j+1)
        # both are equal-> (i+1,j+1)

        # bottom up approach

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1,):
                # if both are equal
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]

                else:
                    # check with all the operation

                    cache[i][j] = 1+min(
                        cache[i+1][j+1],
                        cache[i][j+1],
                        cache[i+1][j],
                    )

        print(cache)
        return cache[0][0]


if __name__ == "__main__":
    word1 = ""
    word2 = "a"
    print(Solution().minDistance(word1, word2))
