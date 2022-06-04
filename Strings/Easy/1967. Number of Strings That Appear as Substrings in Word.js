`Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.

`;

const numOfStrings = (patterns, word) => {
  let count = 0;

  for (let i = 0; i < patterns.length; i++) {
    if (word.includes(patterns[i])) {
      count++;
    }
  }
  return count;
};

console.log(numOfStrings(["a", "b", "c"], "aab"));
