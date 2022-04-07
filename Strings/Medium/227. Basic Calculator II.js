`
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5

`;
const calculate = (s) => {
  if (s == null || s.length === 0) return null;

  // remove space
  s = s.replace(/\s/g, "");

  let stack = []; // stack for operations
  let n = 0;
  let sign = "+";

  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    // number
    if (/\d/.test(c)) n = n * 10 + Number(c); // e.g. '14' -> 1 * 10 + 4
    console.log({ test: /\d/.test(c), n }, c);
    // sign or last number
    if (/\D/.test(c) || i === s.length - 1) {
      console.log({ inside: c });
      if (sign === "-") stack.push(-n);
      else if (sign === "+") stack.push(n);
      else if (sign === "*") stack.push(stack.pop() * n);
      else if (sign === "/") stack.push(stack.pop() / n);

      sign = c;
      n = 0;
    }

    console.log({ c, n, sign, stack });
  }
  return stack.reduce((a, b) => a + b);
};
s = "3+2*2";
const result = calculate(s);
console.log(result);
