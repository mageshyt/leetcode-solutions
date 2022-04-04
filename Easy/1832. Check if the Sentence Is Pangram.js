`A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false`;

const checkIfPangram = (sentence) => {
  const alp_arr = new Array(26).fill(0);
  for (let i = 0; i < sentence.length; i++) {
    alp_arr[sentence.charCodeAt(i) - 97]++;
  }
  for (let i = 0; i < alp_arr.length; i++) {
    if (alp_arr[i] === 0) {
      return false;
    }
  }
    return true;
};
console.log(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"));
