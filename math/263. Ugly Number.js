`An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.`;

const isUgly = (num) => {
  const primeFactors = [2, 3, 5];
  for (let i = 0; i < num; i++) {
    while (num % primeFactors[i] === 0) {
      num = num / primeFactors[i];
    }
  }
  return num === 1;
};
console.log(isUgly(6));
