`Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0`;

const addDigits = (num) => {
  let result = Infinity;
  if (num === 0) return 0; // Edge case
  while (true) {
    if (result < 10) return result;
    digVal = (num % 10) + Math.floor(num / 10);  // Get the last digit and quotient
    result = digVal;
    num = digVal;
  }
};
console.log(addDigits(1111));
