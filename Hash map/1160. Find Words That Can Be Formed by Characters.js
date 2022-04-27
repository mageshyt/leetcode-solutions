`You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.`;

const countCharacters = (words, chars) => {
  let map = new Map();
  for (let char of chars) {
    map.set(char, (map.get(char) || 0) + 1);
  }
  let res = 0;
  for (let word of words) {
    let temp = new Map(map);
    let flag = true;
    for (let char of word) {
      if (temp.get(char) > 0) {
        temp.set(char, temp.get(char) - 1);
      } else {
        flag = false;
        break;
      }
    }

    if (flag) {
      res += word.length;
    }
  }
  return res;
};
words = ["cat", "bt", "hat", "tree"];
chars = "atach";
console.log(countCharacters(words, chars));
