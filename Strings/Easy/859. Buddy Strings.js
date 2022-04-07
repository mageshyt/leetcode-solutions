`Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.`;
const buddyStrings = (s, goal) => {
  if (s.length !== goal.length) return false;
  let left = 0;
  let right = goal.length - 1;
  let count = 0;
  while (left < goal.length) {
    if (s[left] !== goal[right]) count++;
    left++;
    right--;
  }
  if (count > 2) return false;
  return count === 0;
};
console.log(buddyStrings("ab", "ba"));
console.log(buddyStrings("aa", "aa"));
(s = "ab"), (goal = "ab");
console.log(buddyStrings(s, goal));
