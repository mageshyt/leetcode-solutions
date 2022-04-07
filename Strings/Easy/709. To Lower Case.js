`Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"`;

const toLowerCase = (s) => {
  const s_array = s.split("");
  for (const char of s_array) {
    if (char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90) {
      s_array[s_array.indexOf(char)] = char.toLowerCase();
    }
  }
  return s_array.join("");
};

console.log(toLowerCase("LOVELY"));
console.log(toLowerCase("Hello"));
console.log(toLowerCase("here"));
