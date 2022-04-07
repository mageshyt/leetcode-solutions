`Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true`;
const arrayStringsAreEqual = (word1, word2) => {
  let word_1_combined = "";
  let word_2_combined = "";
  for (let i = 0; i < word1.length; i++) {
    word_1_combined += word1[i];
  }
  for (let i = 0; i < word2.length; i++) {
    word_2_combined += word2[i];
  }
  console.log(word_1_combined, word_2_combined);
  return word_1_combined === word_2_combined;
};
console.log(arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]));
