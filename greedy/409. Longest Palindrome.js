`Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2`;

const longestPalindrome = (s) => {
  const char_tracker = new Map();
  for (let char of s) {
    char_tracker.set(char, char_tracker.get(char) + 1 || 1);
  }

  let max_length = 0;
  for (let [key, value] of char_tracker) {
    max_length += Math.floor(value / 2) * 2;
    `
    example:
    abccccdd
     here a --> 1 and if we do 1/2 * 2 then we get 2 next if case will work if we have even number of char 
    
    `;
    if (max_length % 2 === 0 && value % 2 === 1) {
      max_length += 1;
    }
  }
  return max_length;
};
console.log(longestPalindrome("abccccdd"));

console.log(longestPalindrome("a"));
