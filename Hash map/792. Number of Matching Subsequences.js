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

const numMatchingSubseq = (s, words) => {
  const map = {};
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (map[char]) {
      map[char].push(i);
    } else {
      map[char] = [i];
    }
  }

  const isSubsequence = (word, map) => {
    let flag = -1;
    for (let char of word) {
      flag = map[char]?.find((i) => i > flag);
      if (flag === undefined) return false; //! if the char not found then return false
    }

    return true;
  };

  // ! loop thourgh the words
  let count = 0;
  for (let word of words) {
    if (isSubsequence(word, map)) {
      count++;
    }
  }

  return count;
};

s = "abcde";
words = ["a", "bb", "acd", "ace"];
console.log(numMatchingSubseq(words, s));
