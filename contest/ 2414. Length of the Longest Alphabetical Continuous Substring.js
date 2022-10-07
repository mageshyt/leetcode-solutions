`An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

    For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.

Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

 

Example 1:

Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.

Example 2:

Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.
`;

const longestContinuousSubstring = (s) => {
  let res = 0;
  let left = 0;
  let right = 1;
  if (s.length === 1) return 0;
  while (right < s.length) {
    if (s[right].charCodeAt(0) - s[right - 1].charCodeAt(0) === 1) {
      right++;
      res = Math.max(res, right - left);
    } else {
      res = Math.max(res, right - left);
      left = right;
      right++;
    }
  }
  return res;
};

console.log(longestContinuousSubstring("abacaba"));
console.log(
  longestContinuousSubstring(
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
  )
);

console.log(longestContinuousSubstring("awy"));
