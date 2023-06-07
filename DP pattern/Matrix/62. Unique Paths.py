
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n  # last rows always 1

        for i in range(m-1):  # start from second last row
            newRow = [1]*n

            for j in range(n-2, -1, -1):  # start from second last column
             
                newRow[j] = newRow[j+1]+row[j]  # add right and bottom

            row = newRow  # update row

        return row[0]  # return first element




# Time complexity: O(2^(m+n))

# Space complexity: O(m+n)

print(Solution().uniquePaths(3, 7))
