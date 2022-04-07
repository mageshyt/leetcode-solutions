`Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"`;

const removeDuplicateLetters = (s) => {
  const results = [];
  const map = {};
  for (let i = 0; i < s.length; i++) {
    map[s[i]] = i;
  }
  for (let i = 0; i < s.length; i++) {
    if (results.includes(s[i])) {
      continue;
    }
    console.log({
      map,
      results,
      char: s[i],
      s,
      res: results[results.length - 1],
      cond: s[i] < results[results.length - 1],
    });
    while (
      results.length > 0 &&
      s[i] < results[results.length - 1] &&
      map[results[results.length - 1]] > i
    ) {
      results.pop();
    }
    results.push(s[i]);
  }
  return results.join("");
};

// console.log(removeDuplicateLetters("bcabc"));
console.log(removeDuplicateLetters("cbacdcbc"));
