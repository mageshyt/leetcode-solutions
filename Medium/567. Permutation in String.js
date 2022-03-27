`Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false`;

const checkInclusion = (s1, s2) => {
  // ! edge case
  if (s1.length > s2.length) return false;
  const count_of_s1 = Array(26).fill(0);
  const count_of_s2 = Array(26).fill(0);
  for (let i = 0; i < s1.length; i++) {
    count_of_s1[s1.charCodeAt(i) - 97]++;
    count_of_s2[s2.charCodeAt(i) - 97]++;
  }
  let matches = 0;
  for (let i = 0; i < 26; i++) {
    if (count_of_s1[i] === count_of_s2[i]) matches++;
  }
  let left = 0;
  for (let right = s1.length; right < s2.length; right++) {
    if (matches === 26) return true;
    let idx = s2.charCodeAt(right) - 97;
    count_of_s2[idx]++;
    if (count_of_s1[idx] === count_of_s2[idx]) matches++;
    else if (count_of_s1[idx] + 1 === count_of_s2[idx]) matches--;

    let idx2 = s2.charCodeAt(left) - 97;
    count_of_s2[idx2]--;
    if (count_of_s1[idx2] === count_of_s2[idx2]) matches++;
    else if (count_of_s1[idx2] - 1 === count_of_s2[idx2]) matches--;
    left++;
  }
  return false;
};
console.log(checkInclusion("ab", "eidbaooo"));
