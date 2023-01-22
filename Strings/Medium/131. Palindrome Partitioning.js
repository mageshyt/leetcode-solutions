`Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 `;

const isPalindrome = (s) => s === s.split("").reverse().join("");

const partition = (s) => {
  const res = [];
  const part = []; // current partition

  const dfs = (start) => {
    if (start >= s.length) {
      res.push([...part]);
      return;
    }

    for (let i = start; i < s.length; i++) {
      if (isPalindrome(s.substring(start, i + 1))) {
        part.push(s.substring(start, i + 1));
        dfs(i + 1);
        part.pop();
      }
    }
  };

  dfs(0);

  return res;
};

console.log("👉 Output:", partition("aab"));
