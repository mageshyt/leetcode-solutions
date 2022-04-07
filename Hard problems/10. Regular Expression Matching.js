`
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
`;

const isMatch = (s, p) => {
  const hash = new Map();
  const backTrack = (i, j) => {
    if (hash.has(`${i}-${j}`)) return hash.get(`${i}-${j}`);
    if (s.length <= i && j >= p.length) return true;
    if (j >= p.length) return false;

    const match = i < s.length && (s[i] === p[j] || p[j] === ".");
    console.log({ i, j, match, hash, s: s[i], p: p[j] });
    if (p[j + 1] === "*" && j + 1 < p.length) {
      console.log("inner", i, j);
      hash.set(
        `${i}-${j}`,
        backTrack(i, j + 2) || (match && backTrack(i + 1, j))
      );
      return hash.get(`${i}-${j}`);
      // !first part is not going use * and second part is going to use *
    }
    if (match) {
      hash.set(`${i}-${j}`, backTrack(i + 1, j + 1));

      return hash.get(`${i}-${j}`);
    }
    hash.set(`${i}-${j}`, false);
    return false;
  };

  return backTrack(0, 0);
};

// console.log(isMatch("aa", "a"));
// console.log(isMatch("aa", "a*"));
console.log(isMatch("ab", ".*"));
