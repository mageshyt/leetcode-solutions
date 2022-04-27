`Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

 

Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
Example 2:

Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.
Example 3:

Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".`;

const countWords = (words1, words2) => {
  const map1 = new Map();
  const map2 = new Map();
  let count = 0;
  for (let i = 0; i < words1.length; i++) {
    const current = words1[i];
    map1.set(current, map1.get(current) + 1 || 1);
  }

  for (let i = 0; i < words2.length; i++) {
    const current = words2[i];
    map2.set(current, map2.get(current) + 1 || 1);
  }
  for (let word of words1) {
    if (map2.get(word) === 1 && map1.get(word) === 1) {
      count++;
    }
  }
  return count;
};
console.log(
  countWords(
    ["leetcode", "is", "amazing", "as", "is"],
    ["amazing", "leetcode", "is"]
  )
);
