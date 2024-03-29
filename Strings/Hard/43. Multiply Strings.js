`Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"`;

const multiply = (num1, num2) => {
  let result = "";
  let i = num1.length - 1;
  let j = num2.length - 1;

  while (i >= 0 || j >= 0) {
    let sum = 0;
    let carry = 0;
    let k = j;
    while (k >= 0) {
      let sum1 = i >= 0 ? num1[i] - "0" : 0;
      let sum2 = num2[k] - "0";
      let sum3 = sum1 * sum2 + carry;
      sum = (sum3 % 10) + sum;
      carry = Math.floor(sum3 / 10);
      k--;
    }
    if (carry > 0) {
      sum = carry + sum;
    }
    result = sum + result;
    i--;
    j--;
  }

  return result;
};
console.log(multiply("2", "3"));
