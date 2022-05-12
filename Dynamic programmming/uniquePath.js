`[0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down`;

const uniquePaths = (m, n, cache = {}) => {
  const key = `${m},${n}`;
  if (key in cache) {
    return cache[key];
  }
  if (m === 1 || n === 1) return 1;
  if (n === 0 || m === 0) return 0;

  const result = uniquePaths(m - 1, n, cache) + uniquePaths(m, n - 1, cache);

  cache[key] = result;
  return result;
};

console.log(uniquePaths(3, 7));
