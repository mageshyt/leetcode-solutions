class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        # insert -> (i , j+1)
        # delete -> (i+1,j)
        # replace -> (i+1,j+1)
        # both are equal-> (i+1,j+1)

        def dfs(i, j):
            ans = 0
            print(i, j, len(word1), len(word2))
            # base case
            if i == len(word1) and j == len(word2):
                return 0

            if i == len(word1):

                # when i is out of bound
                # then max operation is to insert all the remaining characters
                return len(word2)-j

            if j == len(word2):
                # when j is out of bound
                # then max operation is to delete all the remaining characters
                return len(word1)-i

            if (i, j) in dp:
                return dp[(i, j)]

            # recursive case

            # case 1 : if both are equal then move on
            if word1[i] == word2[j]:

                ans = dfs(i+1, j+1)

            else:
                ans = 1+min(
                    dfs(i+1, j),
                    dfs(i, j+1),
                    dfs(i+1, j+1)
                )

            dp[(i, j)] = ans
            return dp[(i, j)]

        return dfs(0, 0)


if __name__ == "__main__":
    word1 = "abc"
    word2 = "yabd"
    print(Solution().minDistance(word1, word2))
