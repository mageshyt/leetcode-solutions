import collections


class Solution:
    def equalPairs(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        hash_map = {}
        res = 0
        for row in grid:
            # hash map to store the number of each row
            hash_map[str(row)] = hash_map.get(str(row), 0) + 1

        for col in range(cols):
            column = []  # store the number of each column
            for row in range(rows):
                # print(row)
                column.append(grid[row][col])

            res += hash_map.get(str(column), 0) # if the column is in the hash map, add the number of the column to res

        return res


grid = [[13, 13], [13, 13]]


print(Solution().equalPairs(grid))
