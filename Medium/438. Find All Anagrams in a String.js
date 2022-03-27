`Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".`;

const findAnagrams = (s, p) => {
  const p_hash = new Set();
  const s_hash = new Set();

  const result = [];
  for (let i = 0; i < p.length; i++) {
    if (!p_hash.has(p[i])) {
      p_hash.add(p[i], 0);
    } else {
      p_hash.add(p[i], p[i]++);
    }
  }
  // compare two hash
  console.log(p_hash, s_hash);
};
console.log(findAnagrams("cbaebabacd", "abc"));
