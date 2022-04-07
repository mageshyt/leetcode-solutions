`Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.`;

const minWindow = (s, t) => {
  if (t === "") return "";
  const T_count = new Map();
  const window_s = new Map();
  for (let char of t) {
    T_count.set(char, (T_count.get(char) || 0) + 1);
  }
  current_have = 0;
  needed = T_count.size;
  for (let i = 0; i < s.length; i++) {
    curr_char = s[i];
    window_s.set(curr_char, (window_s.get(curr_char) || 0) + 1);
    if (
      T_count.has(curr_char) &&
      window_s.get(curr_char) === T_count.get(curr_char)
    ) {
      current_have++;
    }
    if (current_have === needed) {
        // Need to update our result
        
    }
  }
};
console.log(minWindow("ADOBECODEBANC", "ABC"));
