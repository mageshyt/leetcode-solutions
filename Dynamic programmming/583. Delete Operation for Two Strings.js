`Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
`;

const minDistance = (word1, word2) => {
  let dp = new Array(word2.length + 1);
  for (let i = 0; i <= word2.length; i++) {
    const temp = new Array(word1.length + 1);

    for (let j = 0; j <= word1.length; j++) {
      if (i === 0 || j === 0) {
        temp[j] = j + i;
      } else if (word1[j - 1] === word2[i - 1]) {
        temp[j] = dp[j - 1];
      } else {
        temp[j] = 1 + Math.min(dp[j], temp[j - 1]);
      }
    }
    dp = temp;
  }

  return dp[word1.length];
};

console.log(minDistance("sea", "eat"));
// console.log(minDistance("leetcode", "etco"));

//! solution 2
