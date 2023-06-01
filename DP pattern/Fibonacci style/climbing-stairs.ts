// tabulation

function climbStairs(n: number): number {
  const dp = new Array(n + 1).fill(0);

  dp[0] = 1; // base case
  dp[1] = 1; // base case
  // [1,_,_] one step
  // [1,1,_,_] two steps

  for (let i = 2; i <= n; i++) {
    // formula: dp[i] = dp[i-1] + dp[i-2] previous two steps

    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
}

console.log(climbStairs(6));

// top down

function climbStairs2(n: number): number {
  const memo = {};

  const helper = (n: number) => {
    if (n === 0 || n === 1) return 1;

    if (memo[n]) return memo[n];

    memo[n] = helper(n - 1) + helper(n - 2);

    return memo[n];
  };

  return helper(n);
}

console.log(climbStairs2(6));
