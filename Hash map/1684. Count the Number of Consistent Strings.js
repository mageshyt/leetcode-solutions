`You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.`;

const countConsistentStrings = (allowed, words) => {
  const map = new Map();
  for (let char of allowed) {
    map.set(char, true);
  }
  let count = 0;
  for (let word of words) {
    let flag = true;
    for (let char of word) {
      if (!map.get(char)) {
        flag = false;
        break;
      }
    }
    if (flag) {
      count++;
    }
  }
  return count;
};
console.log(countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]));
