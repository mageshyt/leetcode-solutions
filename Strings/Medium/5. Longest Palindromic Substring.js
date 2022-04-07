`Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
`;
const longestPalindrome = (s) => {
  let longest = "";
  for (let i = 0; i < s.length; i++) {
    let left = i;
    let right = i;
    while (left >= 0 && right < s.length) {
      if (s[left] === s[right]) {
        if (right - left + 1 > longest.length) {
          longest = s.slice(left, right + 1);
        }
        left--;
        right++;
      } else {
        break;
      }
    }
  }
  return longest;
};
console.log(longestPalindrome("babad"));
