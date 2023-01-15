const longestCommonSubsequence = (str1, str2) => {
  const dp = new Array(str2.length + 1)
    .fill(0)
    .map(() => new Array(str1.length + 1).fill(0));

  //! bottom up solution
  for (let i = str1.length - 1; i >= 0; i--) {
    for (let j = str2.length - 1; j >= 0; j--) {
      // if both the char are equal
      if (str1[i] === str2[j]) {
        dp[j][i] = dp[j + 1][i + 1] + 1;
        `
            if the char are equal then add 1+ diagonal value 
            diagonal --> (j+1, i+1)
        `;
      }
      // if the char are not equal
      else {
        dp[j][i] = Math.max(dp[j][i + 1], dp[j + 1][i]);
        `
         if they are not equal then  then take the max of the right and diagonal value
        `;
      }
    }
  }
  return dp[0][0];
};

console.log(longestCommonSubsequence("sea", "eat"));

const solution2 = (str1, str2) => {
  const dp = new Array(str2.length + 1)
    .fill(0)
    .map(() => new Array(str1.length + 1).fill(0));

  //! top down solution
  const helper = (i, j) => {
    if (i === str1.length || j === str2.length) return 0;
    if (dp[j][i] !== 0) return dp[j][i];
    if (str1[i] === str2[j]) {
      dp[j][i] = helper(i + 1, j + 1) + 1;
    } else {
      dp[j][i] = Math.max(helper(i + 1, j), helper(i, j + 1));
    }
    return dp[j][i];
  };
  return helper(0, 0);
};

console.log(solution2("sea", "eat"));
