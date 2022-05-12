`Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045`;

const countVowelStrings = (n) => {
  if (n === 1) return 5;
  let a = 1;
  let e = 1;
  let i = 1;
  let o = 1;
  let u = 1;
  const increment = () => {
    a = a + e + i + o + u;
    e = e + i + o + u;
    i = i + o + u;
    o = u + o;
    u = 1;
  };
  for (let j = 2; j <= n; j++) {
    increment();
  }

  return a + e + i + o + u;
};

console.log(countVowelStrings(1));
console.log(countVowelStrings(2));
console.log(countVowelStrings(3));
