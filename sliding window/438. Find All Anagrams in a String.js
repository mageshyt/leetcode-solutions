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

const isEqual = (map1, map2) => {
  for (let key in map1) {
    if (map1[key] !== map2[key]) {
      return false;
    }
  }
  return true;
};
const buildMap = (str, len) => {
  let map = {};
  for (let i = 0; i < len; i++) {
    if (map[str[i]]) {
      map[str[i]]++;
    } else {
      map[str[i]] = 1;
    }
  }
  return map;
};
const findAnagrams = (s, p) => {
  let res = [];
  //! Edge case
  if (s.length < p.length) return res;
  //! Create a hashmap of p
  let P_map = buildMap(p, p.length);

  let windowStart = 0;

  for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
    const word = s.slice(windowStart, p.length + windowEnd);
    //! Create a hashmap of word
    let map = buildMap(word, p.length);
    //! Check if the hashmap is equal to P_map
    if (isEqual(P_map, map)) {
      res.push(windowStart);
    }
    windowStart++;
    //! Move the window
  }
  return res;
};
console.log(findAnagrams("cbaebabacd", "abc"));
console.log(findAnagrams("abab", "ab"));
``
