`You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
`;

const longestPalindrome = (words) => {
  const map = {};
  let len = 0;

  // ! find mirror word alone form the words
  for (let word of words) {
    const mirror = reverse(word);
    if (map[word]) {
      // mins the count
      map[word]--;
      len += 4;
    } else {
      map[mirror] = map[mirror] ? map[mirror] + 1 : 1;
    }
  }
  const morePal = Object.keys(map).filter(
    (word) => map[word] && reverse(word) === word
  );
  // ! if we have any values then add 2 to counter
  if (morePal.length) len += 2;
  return len;
};
const reverse = (word) => word.split("").reverse().join("");

console.log(longestPalindrome(["lc", "cl", "gg"]));
console.log(longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]));
console.log(longestPalindrome(["cc", "cc"]));
