`Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
`;

const findAllConcatenatedWordsInADict = (words) => {
  const wordSet = new Set(words);

  const dp = new Map();

  const dfs = (word) => {
    if (dp.has(word)) return dp.get(word);

    for (let i = 1, len = word.length; i < len; i++) {
      const prefix = word.slice(0, i); // prefix
      const suffix = word.slice(i); // suffix

      // if th prefix is in the wordSet and the suffix is in the wordSet or the suffix can be further divided

      if (wordSet.has(prefix) && (wordSet.has(suffix) || dfs(suffix))) {
        // console.log("👉 word ", word);
        // console.log("👉 prefix", prefix);
        // console.log("👉 suffix", suffix);

        // console.log("-----------------");
        return true;
      }
    }

    dp.set(word, false);
    return false;
  };

  const res = [];
  for (let word of words) {
    // console.log("👉 word", word);
    if (dfs(word)) {
      //   console.log(
      //     "🚀 ~ file: 472. Concatenated Words.js ~ line 47 ~ word",
      //     word
      //   );
      res.push(word);
    } else {
      //   console.log( "🚀 ~ file: 472. Concatenated Words.js ~ line 47 ~ word",
      //     word
      //   );
    }
  }

  return res;
};

const words = [
  "cat",
  "cats",
  "catsdogcats",
  "dog",
  "dogcatsdog",
  "hippopotamuses",
  "rat",
  "ratcatdogcat",
];

findAllConcatenatedWordsInADict(words);
