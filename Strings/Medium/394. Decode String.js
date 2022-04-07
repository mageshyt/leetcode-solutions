`Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
`;
function isNumeric(num) {
  return !isNaN(num);
}
const decodedString = (s) => {
  const stack = []; // stack to store the result
  curString = ""; // final string
  curNumber = 0;
  for (let char of s) {
    console.log({ char, curString, curNumber, stack });
    if (char === "[") {
      stack.push(curString); // push the character
      stack.push(curNumber); // push the number
      curString = ""; // reset the string
      curNumber = 0; // reset the number
    } else if (char === "]") {
      let num = stack.pop(); // pop the number
      let prevString = stack.pop(); // pop the string
      curString = prevString + curString.repeat(num);
    } else if (isNumeric(char)) {
      curNumber = curNumber * 10 + parseInt(char);
    } else {
      curString += char; // add the character to the string
    }
  }
  return curString;
};

const decodedStr = decodedString("100[leetcode]");
console.log(decodedStr);
