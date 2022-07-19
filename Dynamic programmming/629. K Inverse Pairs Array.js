`For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.`;

const kInversePairs = (n, k) => {
  const mod = 1e9 + 7;

  let dp = Array(k + 1).fill(0);

  for (let i = 0; i <= n; ++i) {
    const temp = new Array(k + 1).fill(0);
    temp[0] = 1; //! make the first element 1
    for (let j = 1; j <= k; ++j) {
      const val = (dp[j] + mod - (j - i >= 0 ? dp[j - i] : 0)) % mod;
      temp[j] = (temp[j - 1] + val) % mod;
    }
    dp = temp;
  }

  return (dp[k] + mod - (k > 0 ? dp[k - 1] : 0)) % mod;
};

console.log(kInversePairs(1000, 1000));
