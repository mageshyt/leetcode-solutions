// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.

// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false
// Example 4:

// Input: s = "([)]"
// Output: false
// Example 5:

// Input: s = "{[]}"
// Output: true
//!------------------------------------------------------------------------------------------------

//* Step 1:
"Create a stack and push ({[ into it";

// var isValid = function (s) {
//   const stack = [];
//   const dictionary = {
//     "}": "{",
//     ")": "(",
//     "]": "[",
//   };
//   for (let i = 0; i < s.length; i++) {
//     let currentChar = s[i];
//     let delChar = dictionary[currentChar];
//     let lastChar = stack[stack.length - 1];
//     if (delChar) {
//       if (delChar === lastChar) {
//         stack.pop();
//       } else {
//         return false;
//       }
//     } else {
//       stack.push(currentChar);
//     }
//   }

//   console.log(stack);
//   return !stack.length;
//   //   if (stack.length === 0) return true;
// };

//!------------------------------------------------------------------------------------------------
var isValid = function (s) {
  const dictionary = {
    "}": "{",
    ")": "(",
    "]": "[",
  };
  const stack = [];
  for (char of s) {
    if (char in dictionary && stack.length > 0) {
      let remove = stack.pop();
      if (remove !== dictionary[char]) {
        return false;
      }
    } else {
      stack.push(char);
    }
  }

  return !stack.length;

  if (stack.length === 0) return true;
};

s = "([])";
console.log(isValid(s));
