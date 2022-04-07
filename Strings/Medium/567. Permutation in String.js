`Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 `;

const checkInclusion = (s1, s2) => {
  for (let i = 0; i < s2.length; i++) {
    const currChar = s2[i];
    // console.log({ currChar });
    if (s1.indexOf(currChar) !== -1) {
      const check = s2.slice(i, i + s1.length);
      console.log({ i, s2: s2.length, s1: s1.length });
      console.log(s1.indexOf(currChar), check);
    }
  }
};
(s1 = "ab"), (s2 = "eidbaooo");
console.log(checkInclusion(s1, s2));
