const integerBreak = (n) => {
  const dp = {};

  const helper = (target) => {
    // base case

    if (target == 0) {
      return 1;
    }

    if (dp[target]) {
      return dp[target];
    }

    let max = 0;

    for (let i = 1; i < target; i++) {
      max = Math.max(max, i * helper(target - i), i * (target - i));
    }

    dp[target] = max;
    return max;
  };

  return helper(n);
};

console.log("👉 res", integerBreak(10));
