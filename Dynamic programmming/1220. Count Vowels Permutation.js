`Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68`;

const countVowelPermutation = (n) => {
  const mod = 10 ** 9 + 7;

  const dp = [[], [1, 1, 1, 1, 1]];

  const a = 0,
    e = 1,
    i = 2,
    o = 3,
    u = 4;
  for (let idx = 2; idx <= n; idx++) {
    dp.push([0, 0, 0, 0, 0]);

    dp[idx][a] = (dp[idx - 1][e] + dp[idx - 1][u] + dp[idx - 1][i]) % mod; //! a can be followed by e, u, i
    dp[idx][e] = (dp[idx - 1][a] + dp[idx - 1][i]) % mod; //! e can be followed by a, i

    dp[idx][i] = (dp[idx - 1][e] + dp[idx - 1][o]) % mod; //! i can be followed by e, o
    dp[idx][o] = dp[idx - 1][i]; //! o can be followed by i
    dp[idx][u] = (dp[idx - 1][i] + dp[idx - 1][o]) % mod; //! u can be followed by i, o
  }

  return dp[n].reduce((a, b) => a + b, 0) % mod;
};

console.log(countVowelPermutation(2)); // 5
