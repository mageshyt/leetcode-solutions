`Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0`;
const isPrime = (n) => {
  if (n < 2) return false;
  for (let i = 2; i < n; i++) {
    if (n % i === 0) return false; // if it is divisible by any number other than 1 and itself, it is not a prime number
  }
  return true; // if it is not divisible by any number other than 1 and itself, it is a prime number
};
const countPrimes = (n) => {
  let count = 0; // count of prime numbers
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      // if isPrime returns true, count will be incremented by 1
      count++;
    }
  }
  return count;
};
n = 499979;
console.log(countPrimes(n));
