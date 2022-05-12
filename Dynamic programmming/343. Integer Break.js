`Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3  × 4 = 36.`;

const integerBreak = (n) => {
  const hash = new Map();
  hash.set(1, 1);

  const helper = (num) => {
    if (num === 1) return 1;
    if (hash.has(num)) return hash.get(num);
    let max = n === num ? 0 : num;
    for (let i = 1; i < num; i++) {
      const val = helper(num - i) * helper(i);
      max = Math.max(max, val);
    }
    hash.set(n, max);
    return max;
  };
  return helper(n);
};
// console.log(integerBreak(19));

//! solution 2

const integerBreak2 = (n) => {
  const hash = new Map();
  hash.set(1, 1);

  for (let i = 2; i <= n; i++) {
    let max = n === i ? 0 : i;
    for (let j = 1; j < i; j++) {
      const val = hash.get(i - j) * hash.get(j);
      max = Math.max(max, val);
    }
    hash.set(i, max);
  }
  return hash.get(n);
};

console.log(integerBreak2(19));
