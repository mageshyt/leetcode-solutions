`Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0`;

const longestValidParentheses = (s) => {
  let left = 0;
  let right = 0;
  const len = s.length;
  let max = 0;
  for (let i = 0; i < len; i++) {
    const curr = s[i];
    if (curr === "(") {
      left++;
    } else if (curr === ")") {
      right++;
    }
    if (left === right) {
      max = Math.max(max, 2 * right);
    } else if (right > left) {
      left = 0;
      right = 0;
    }
  }
  //! right scan
  left = 0;
  right = 0;
  for (let i = len - 1; i >= 0; i--) {
    const curr = s[i];
    if (curr === "(") {
      left++;
    } else if (curr === ")") {
      right++;
    }
    if (left === right) {
      max = Math.max(max, 2 * left);
    }
    if (left > right) {
      left = 0;
      right = 0;
    }
  }
  return max;
};

console.log(longestValidParentheses(")()())"));
