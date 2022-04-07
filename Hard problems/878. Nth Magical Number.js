`A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2
Example 2:

Input: n = 4, a = 2, b = 3
Output: 6
`;
const nthMagicalNumber = (n, a, b) => {
  let res = 0;
  while (true) {
    res = n;
    console.log({ re1: n % a, re2: n % b, a, b, n });
    if (n % a === 0 && n % b === 0) return n;
    n++;
  }
};
console.log(nthMagicalNumber(1, 2, 3));
