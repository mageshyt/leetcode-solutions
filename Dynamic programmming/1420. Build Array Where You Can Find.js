const numOfArrays = (n, m, k) => {
  const MOD = 10 ** 9 + 7;
  const dp = {};

  const dfs = (i, max_so_far, remain) => {
    if (i === n) {
      return remain === 0 ? 1 : 0;
    }

    const key = `${i}-${max_so_far}-${remain}`;

    if (dp[key]) {
      return dp[key];
    }

    let result = (max_so_far * dfs(i + 1, max_so_far, remain)) % MOD;

    for (let j = max_so_far + 1; j <= m; j++) {
      result = (result + dfs(i + 1, j, remain - 1)) % MOD;
    }

    dp[key] = result;

    return result;
  };
  return dfs(0, 0, k);
};

console.log(numOfArrays(9, 1, 1)); // 6
