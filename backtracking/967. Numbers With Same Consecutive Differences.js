`Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

 

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
`;

const numsSameConsecDiff = (n, k) => {
  const res = [];

  let start = new Array(n).fill(0);
  start[0] = 1;
  start = parseInt(start.join(""));
  const end = start * 10 - 1;

  for (let i = start; i <= end; i++) {
    const digits = i.toString().split("");
    let valid = true;
    for (let j = 0; j < digits.length - 1; j++) {
      if (Math.abs(digits[j] - digits[j + 1]) !== k) {
        valid = false;
        break;
      }
    }
    if (valid) res.push(i);
  }
  return res;
};
// console.log(numsSameConsecDiff(9, 9));

// ! optimize
const numsSameConsecDiff2 = (n, k) => {
  const res = [];
  const dfs = (num) => {
    if (num.toString().length === n) {
      res.push(num);
      return;
    }
    const lastDigit = num % 10;
    if (lastDigit - k >= 0) dfs(num * 10 + lastDigit - k);
    if (k > 0 && lastDigit + k < 10) dfs(num * 10 + lastDigit + k);
  };
  for (let i = 1; i < 10; i++) {
    dfs(i);
  }
  return res;
};

console.log(numsSameConsecDiff2(9, 9));
