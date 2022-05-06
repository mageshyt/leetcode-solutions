`Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
`;

const isInterleave = (s1, s2, s3) => {
  s1_len = s1.length;
  s2_len = s2.length;
  s3_len = s3.length;
  //!edge case
  if (s1_len + s2_len !== s3_len) return false;
  if (s1_len === 0 && s2_len === 0 && s3_len === 0) return true;

  const table = new Array(s1_len + 1)
    .fill(0)
    .map(() => new Array(s2_len + 1).fill(false));

  for (let i = 0; i < s1_len; i++) {
    for (let j = 0; j < s2_len; j++) {
      if (i === 0 && j === 0) {
        table[i][j] = true;
      } else if (i === 0) {
        table[i][j] = table[i][j - 1] && s2[j - 1] === s3[i + j - 1];
      } else if (j === 0) {
        table[i][j] = table[i - 1][j] && s1[i - 1] === s3[i + j - 1];
      } else {
        table[i][j] =
          (table[i][j - 1] && s2[j - 1] === s3[i + j - 1]) ||
          (table[i - 1][j] && s1[i - 1] === s3[i + j - 1]);
      }
    }
  }
  console.log(table);
  return table[s1_len][s2_len];
};

console.log(isInterleave("aabcc", "dbbca", "aadbbcbcac"));
