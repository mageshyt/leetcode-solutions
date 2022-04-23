`A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".`;



const countGoodSubstrings = (s) => {
  let count = 0;
  const queue = [];

  for (let i = 0; i < s.length; i++) {
    const current = s[i];
    if (!queue.includes(current)) {
      if (queue.length !== 3) {
        queue.push(current);
      }
      if (queue.length === 3) {
        count++;
        queue.shift();
        if (!queue.includes(current)) {
          queue.push(current);
        }
      }
    } else {
      queue.shift();
      if (!queue.includes(current)) {
        queue.push(current);
      }
    }
  }
  return count;
};
console.log(countGoodSubstrings("xyzzaz"));
