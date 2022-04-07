`
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1


`;
const happyNumber = (n) => {
  const arr = [];
  while (n !== 1) {
    let sum = 0;
    while (n > 0) {
      sum += Math.pow(n % 10, 2);
      n = Math.floor(n / 10);
    }
    n = sum;
    if (arr.includes(n)) {
      // if the number is repeated then return false because if wont form 1
      return false;
    }
    arr.push(n);
  }
  return true;
};
console.log(happyNumber(2));
