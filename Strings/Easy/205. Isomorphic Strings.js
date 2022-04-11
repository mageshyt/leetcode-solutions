`Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true`;
const isIsomorphic = (s, t) => {
  const map = new Map();
  for (let i = 0; i < s.length; i++) {
    if (!map.has(s[i])) {
      map.set(s[i], t[i]);
    }
  }
  const map2 = new Map();
  for (let [key, value] of map) {
    if (!map2.has(value)) {
      map2.set(value, key);
    } else {
      return false;
    }
  }
  // console.log(map);
  for (let i = 0; i < t.length; i++) {
    if (map.get(s[i]) !== t[i]) {
      return false;
    }
  }
  return true;
};
console.log(isIsomorphic("foo", "bar"));
console.log(isIsomorphic("egg", "add"));
console.log(isIsomorphic("paper", "title"));
console.log(isIsomorphic("badc", "baba"));
