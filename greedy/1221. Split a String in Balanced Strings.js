`Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".`;
const balancedStringSplit = (s) => {
  let res = 0;
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "L") count++;
    if (s[i] === "R") count--;
    if (count === 0) res++;
  }
  return res;
};
console.log(balancedStringSplit("RLRRLLRLRL"));
