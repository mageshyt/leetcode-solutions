`Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
 `;

const buildSet = (words) => {
  const word_map = [];
  for (let i = 0; i < words.length; i++) {
    const hash = new Set();
    for (let j = 0; j < words[i].length; j++) {
      hash.add(words[i][j]);
    }
    word_map.push(hash);
  }
  return word_map;
};

const HasCommons = (word1, word2) => {
  //! if there is common char return false
  const map = new Map();

  for (let i = 0; i < word1.length; i++) {
    map.set(word1[i], true);
  }
  for (let i = 0; i < word2.length; i++) {
    if (map.has(word2[i])) return false;
  }
  return true;
};

console.log(HasCommons("abcw", "xtfn"));
const maxProduct = (words) => {
  let max = 0;
  let wordMap = buildSet(words);
  for (let i = 0; i < words.length; i++) {
    for (let j = i + 1; j < words.length; j++) {
      if (HasCommons(words[i], words[j])) {
        max = Math.max(max, words[i].length * words[j].length);
      }
    }
  }
  return max;
};

console.log(maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]));

console.log(maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]));
