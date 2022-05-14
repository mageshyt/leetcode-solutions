`Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')`;

const minDistance = (word1, word2) => {
  //! 2d grid
  const table = new Array(word1.length + 1)
    .fill(0)
    .map(() => new Array(word2.length + 1).fill(0));

  const operations = [
    [0, 1], //! insert
    [1, 0], //! delete
    [1, 1], //! replace
  ];

  //   //! working with our base case

  for (let i = 0; i <= word2.length; i++) {
    table[word1.length][i] = word2.length - i;
  }
  for (let i = 0; i <= word1.length; i++) {
    table[i][word2.length] = word1.length - i;
  }

  for (let i = word2.length - 1; i >= 0; i--) {
    for (let j = word1.length - 1; j >= 0; j--) {
      if (word2[i] === word1[j]) {
        table[j][i] = table[j + 1][i + 1];
      } else {
        let minOperations = Infinity;
        for (let [x, y] of operations) {
          minOperations = Math.min(minOperations, table[j + x][i + y] + 1);
        }
        table[j][i] = minOperations;
      }
    }
  }
  return table[0][0];
};
console.log(minDistance("abc", "adc"));
console.log(minDistance("intention", "execution"));

console.log(minDistance("horse", "ros"));
