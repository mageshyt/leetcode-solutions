`Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
 `;

const isEqual = (word1, word2) => {
  const map_1 = new Map();
  const map_2 = new Map();
  for (let i = 0; i < word1.length; i++) {
    const char = word1[i]; //! word1[i] is a char
    const char_2 = word2[i]; //! word2[i] is a char
    if (!map_1.has(char)) {
      map_1.set(char, char_2);
    }
    if (!map_2.has(char_2)) {
      map_2.set(char_2, char);
    }
    if (map_1.get(char) !== char_2 || map_2.get(char_2) !== char) {
      return false;
    }
  }
  return true;
};

const findAndReplacePattern = (words, pattern) => {
  const map = new Map();
  const result = [];
  for (let char of pattern) {
    map.set(char, map.get(char) + 1 || 1);
  }
  for (let word of words) {
    if (isEqual(word, pattern)) {
      result.push(word);
    }
  }

  return result;
};

console.log(
  findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")
);
