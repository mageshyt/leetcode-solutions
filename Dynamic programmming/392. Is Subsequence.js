`Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false`;

const isSubsequence = (s, t) => {
  const max_len = Math.max(s.length, t.length);
  let subsequence = 0;
  for (let i = 0; i < max_len; i++) {
    if (s[subsequence] === t[i]) {
      console.log({ s: s[subsequence], t: t[i] });
      subsequence++;
    }
  }
  return subsequence >= s.length ? true : false;
};

console.log(isSubsequence("abc", "ahbgdc"));
