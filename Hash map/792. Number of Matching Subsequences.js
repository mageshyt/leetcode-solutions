`Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
`;

const numMatchingSubseq = (words, s) => {
  const map = new Map();

  for (let char of s) {
    map.set(char, (map.get(char) + 1) | 1);
  }
  let count = 0;
  for (let word of words) {
    const temp_map = map;
    let flag = true;
    for (let char of word) {
      if (!temp_map.has(char)) {
        flag = false;
      }
      if (temp_map.get(char) >= 0) {
        temp_map.set(char, map.get(char) - 1);
      } else {
        flag = false;
        break;
      }
    }
    if (flag) {
      count++;
    }
  }
  return count;
};
let s = "abcde";
let words = ["a", "bb", "acd", "ace"];

console.log(numMatchingSubseq(words, s));
