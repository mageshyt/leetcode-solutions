`Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

 

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1`;
const countSegments = (s) => {
  s = s.split(" ");
  return s.filter((x) => x !== "").length;
};

console.log(countSegments("Hello, my name is John"));
