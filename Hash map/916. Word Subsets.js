`You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
`;

const wordSubsets = (word1, word2) => {
  const map1 = new Map();
  for (let word of word2) {
    for (let letter of word) {
      if (!map1.has(letter)) {
        map1.set(letter, 0);
      }
      map1.set(letter, map1.get(letter) + 1);
    }
  }

  const result = [];
  for (let word of word1) {
    const map2 = new Map();
    for (let char of word) {
      map2.set(char, map2.get(char) + 1 || 1);
    }
    let isUniversal = true;
    for (let [key, value] of map1) {
      if (!map2.has(key) || map2.get(key) < value) {
        isUniversal = false;
        break;
      }
    }
    console.log({ word, map2 });
    if (isUniversal) {
      result.push(word);
    }
  }
  console.log(map1);
  return result;
};

console.log(
  wordSubsets(
    ["amazon", "apple", "facebook", "google", "leetcode"],
    ["lo", "eo"]
  )
);
[("lo", "eo")];
