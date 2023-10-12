`Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
`;

const integerBreak = (n) => {
  // Object to store memoized values for dynamic programming
  const dp = {};

  const helper = (target) => {
    // Base case: if the target is 0, there's only one way to break it, which is not breaking it at all
    if (target === 0) {
      return 1;
    }

    // If we have already computed the result for this target, return it from the memoized values
    if (dp[target]) {
      return dp[target];
    }

    let max = 0;

    // Iterate through possible breaking points and calculate the maximum product
    for (let i = 1; i < target; i++) {
      max = Math.max(max, i * helper(target - i), i * (target - i));
    }

    // Memoize the maximum product for this target
    dp[target] = max;
    return max;
  };

  // Start the recursive helper function
  return helper(n);
};
