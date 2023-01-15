`An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
`;

const isUgly = (n: number): boolean => {
  //! only for non negative numbers we can use this approach
  if (n <= 0) return false;
  const KeepDividing = (n: number, divisor: number): number => {
    while (n % divisor === 0) {
      n /= divisor;
    }
    return n;
  };
  n = KeepDividing(n, 2);
  n = KeepDividing(n, 3);
  n = KeepDividing(n, 5);

  return n === 1;
};

console.log(isUgly(6));
console.log(isUgly(1));
console.log(isUgly(14));
