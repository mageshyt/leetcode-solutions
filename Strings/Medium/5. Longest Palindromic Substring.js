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
  let resLen = 0;
  for (let i = 0; i < s.length; i++) {
    // * odd palindrome
    //! i is going to be the center of the palindrome
    let left = i;
    let right = i;
    `
    we will move the pointer from center
    `;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (right - left + 1 > resLen) {
        longest = s.slice(left, right + 1);
        resLen = right - left + 1;
      }
      left--; //! move left pointer to left side form center
      right++; //! move right pointer to right side from center
    }

    // * even palindrome
    left = i;
    right = i + 1;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (right - left + 1 > resLen) {
        longest = s.slice(left, right + 1);
        resLen = right - left + 1;
      }
      left--;
      right++;
    }
  }
  return longest;
};
console.log(longestPalindrome("babad"));
