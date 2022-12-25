`Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.`;

const closeStrings = (word1, word2) => {
  // base case
  if (word1.length !== word2.length) return false;
  const map1 = new Map();
  const map2 = new Map();

  for (let i = 0; i < word1.length; i++) {
    map1.set(word1[i], map1.get(word1[i]) + 1 || 1);
    map2.set(word2[i], map2.get(word2[i]) + 1 || 1);
  }

  let values = [...map1.values()];

  for (let char of map2.keys()) {
    //! if key not in map 2
    if (!map1.has(char)) return false;
    const idx = values.indexOf(map2.get(char));
    // if no idx found
    if (idx == -1) return false;
    values.splice(idx, 1);
  }
  return values.length === 0;
};
``;
console.log(closeStrings("cabbba", "abbccc"));
