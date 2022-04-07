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

const buildMap = (str, len) => {
  // Function use to build the hash map
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
// ! function to check two objects are equal
const isEqual = (map1, map2) => {
  for (let key in map1) {
    if (map1[key] !== map2[key]) {
      return false;
    }
  }
  return true;
};

const findAnagrams = (s, p) => {
  if (s.length < p.length) return []; // Edge case
  const result = [];
  const p_count = buildMap(p, p.length);
  const s_count = buildMap(s, p.length);
  if (isEqual(p_count, s_count)) {
    // if the two objects are equal then add 0 to the result
    result.push(0);
  }
  let left_pointer = 0;
  for (let right = p.length; right < s.length; right++) {
    const current_char = s[right]; // our current character
    if (!s_count[current_char]) {
      // if the current character is not in the s_count then add
      s_count[current_char] = 1;
    } else {
      // if it was already in the s_count then increment it
      s_count[current_char]++;
    }
    s_count[s[left_pointer]]--;
    if (s_count[s[left_pointer]] === 0) {
      // if the value is 0 then delete it
      delete s_count[s[left_pointer]];
    }
    left_pointer++;

    if (isEqual(p_count, s_count)) {
      // ! at worst case we will get big O(26)
      result.push(left_pointer);
    }
  }
  return result;
};
console.log(findAnagrams("cbaebabacd", "abc"));
