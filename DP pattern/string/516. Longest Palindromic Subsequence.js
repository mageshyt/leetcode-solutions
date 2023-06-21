const longestPalindromeSubseq = (s) => {
  const dp = {};

  const helper = (left, right) => {
    const key = left + "-" + right;
    if (key in dp) return dp[key];

    if (left > right) return 0;
    if (left === right) return 1;

    if (s[left] === s[right]) {
      dp[key] = 2 + helper(left + 1, right - 1);
    } else {
      dp[key] = Math.max(helper(left + 1, right), helper(left, right - 1));
    }

    return dp[key];
  };
  return helper(0, s.length - 1);
};
s = "abcabcabcabc";
console.log(longestPalindromeSubseq(s));
