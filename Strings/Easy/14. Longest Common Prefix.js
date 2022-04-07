`Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.`;

const longestCommonPrefix = (words) => {
  // !Edge case
  if (words.length === 0) return "";
  let prefix = words[0];
  for (let i = 1; i < words.length; i++) {
    while (words[i].indexOf(prefix) !== 0) {
      // ! when the word index of prefix is 0 then it will end the loop;
      console.log({ a: words[i].indexOf(prefix), prefix, word: words[i] });
      prefix = prefix.substring(0, prefix.length - 1);
    }
  }
  return prefix;
};
strs = ["flower", "flow", "flight"];
console.log(longestCommonPrefix(strs));
