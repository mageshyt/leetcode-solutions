`

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
`;
const IsMatch = (s_len, p_len, s, p, dp) => {
  if (s_len < 0 && p_len < 0) return true; // both are empty then return true
  if (s_len < 0 && p_len > 0) return false; // s length is less than 0 and p length is greater than 0 then return false
  if (s_len >= 0 && p_len < 0) {
    for (let i = 0; i <= s_len; i++) {
      if (s[i] !== "*") return false;
    }
    return true;
  }
  if (dp[s_len][p_len] !== -1) return dp[s_len][p_len];
  const curr_s = s[s_len];
  const curr_p = p[p_len];
  if (curr_p === curr_s || curr_p === "?") {
    return (dp[s_len][p_len] = IsMatch(s_len - 1, p_len - 1, s, p, dp));
  } else if (curr_p === "*") {
    return (dp[s_len][p_len] =
      IsMatch(s_len - 1, p_len, s, p, dp) ||
      IsMatch(s_len, p_len - 1, s, p, dp));
  }
  return false;
};
const wildCard = (s, p) => {
  const s_len = s.length - 1;
  const p_len = p.length - 1;
  dp = {};
  return IsMatch(s_len, p_len, s, p, dp);
};

console.log(wildCard("ca", "*?a"));
