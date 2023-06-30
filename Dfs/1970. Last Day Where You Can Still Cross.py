from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        left = 1
        right = len(cells)

        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            if(self.traverse(row, col, cells, mid)):
                ans = mid
                left = mid+1
            else:
                right = mid - 1

        return ans

    def traverse(self, n: int, m: int, cells: List[List[int]], day: int) -> int:

        # 0 -> land
        # 1 -> water

        grid = [[0]*m for _ in range(n)]

        # 1. find the first row that has land and start dfs from there

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(day):
            row, col = cells[i]

            grid[row-1][col-1] = 1

        visited = set()

        # we need to start from the first row where land is preset
        stack = [(0, col) for col in range(m) if grid[0][col] == 0]

        while stack:

            row, col = stack.pop()

            if row == n-1:
                return True

            if (row, col) in visited:
                continue

            visited.add((row, col))

            for d in direction:
                new_row, new_col = row+d[0], col+d[1]

                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
                    continue

                if grid[new_row][new_col] == 0:
                    stack.append((new_row, new_col))

        return False


if __name__ == "__main__":
    s = Solution()

    row = 3
    col = 3
    cells = [[1, 2], [2, 1], [3, 3], [2, 2], [
        1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
    print(s.latestDayToCross(row, col, cells))
