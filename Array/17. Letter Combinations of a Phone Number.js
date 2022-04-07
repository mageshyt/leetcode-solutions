`Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]`;

const letterCombinations = (digits) => {
  const map = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
  };
  let ans = [];
  if (digits.length === 0) return ans;
  const dfs = (str, idx) => {
    if (idx === digits.length) {
      ans.push(str);
      return;
    }
    for (const char of map[digits[idx]]) {
      dfs(str + char, idx + 1);
    }
  };
  dfs("", 0);
  return ans;
};

console.log(letterCombinations("23"));
