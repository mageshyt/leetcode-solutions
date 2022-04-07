`Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false`;
const isAnagram = (s, t) => {
  if (s.length !== t.length) return false;
  let count = 0;
  const hash = new Map();
  for (let i = 0; i < s.length; i++) {
    hash.set(s[i], hash.get(s[i]) + 1 || 1);
  }
  for (let i = 0; i < t.length; i++) {
    if (hash.has(t[i]) && hash.get(t[i]) > 0) {
      hash.set(t[i], hash.get(t[i]) - 1);
      count++;
    }
  }
  console.log(hash);
  return count === s.length;
};

//! solution 2
const isAnagram2 = (s, t) => {
  const t_temp = t.split("");
  t_temp.sort();
  const s_temp = s.split("");
  s_temp.sort();
  return t_temp.join("") === s_temp.join("");
};
console.log(isAnagram2("anagram", "nagaram"));
