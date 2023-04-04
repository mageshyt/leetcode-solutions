'''
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

 

Example 1:



Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
Example 2:

Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.
Example 3:

Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]
'''


class Solution:
    def findBall(self, grid):

        # idea
        # drop the ball and check at every row if they are stuck or not

        # constraints
        # if c_next < 0 or c_next >= len(grid[0]) or grid[r][c_next] == -grid[r][c]:
        # means if next column is out of bound or if the next column is not equal to the current column then the ball is stuck

        rows = len(grid)
        cols = len(grid[0])
        ans = list(range(cols))

        for r in range(rows):
            print('new \n')
            for i in range(cols):
                print('ans = ', ans)
                c = ans[i]  # current column
                if c == -1:
                    continue  # if the ball is stuck then continue

                c_next = c+grid[r][c]  # next column

                if c_next < 0 or c_next >= cols or grid[r][c_next] == -grid[r][c]:

                    # c next < 0 -> means the ball is stuck on the left wall
                    # c_next >= len(grid[0]) -> means the ball is stuck on the right wall
                    # grid[r][c_next] == -grid[r][c] -> means the ball is stuck in the box \⚾/ [-1,1] or [1,-1]
                    ans[i] = -1
                    continue

                # if the ball is not stuck then move the ball to the next column
                ans[i] += grid[r][c]

        return ans


if __name__ == "__main__":
    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
    print(Solution().findBall(grid))
