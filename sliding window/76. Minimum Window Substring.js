`Given two strings s and t of lengths m and n respectively,
 return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
 If there is no such substring, return the empty string "".

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
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?`;

const minWindow = (s, t) => {
  // ! if t length is greater than s length, return empty string
  if (s.length < t.length) return "";
  const t_map = new Map();
  const window_map = new Map();

  for (const char of t) {
    t_map.set(char, t_map.get(char) + 1 || 1);
  }

  let have = 0;
  let need = t_map.size;

  let resLen = Number.MAX_VALUE;
  let res = [-1, -1];

  let window_start = 0;

  for (let i = 0; i < s.length; i++) {
    const char = s[i];

    if (t_map.has(char)) {
      window_map.set(char, window_map.get(char) + 1 || 1);
      if (window_map.get(char) === t_map.get(char)) {
        have++;
      }
    }
    // ! if have is equal to need, we have a valid window
    while (have === need) {
      //! time to update the result
      if (i - window_start + 1 < resLen) {
        res = [window_start, i];
        resLen = i - window_start + 1;
      }
      //! now we are going to pop the char from left
      const leftChar = s[window_start];
      if (t_map.has(leftChar)) {
        window_map.set(leftChar, window_map.get(leftChar) - 1);
        if (window_map.get(leftChar) < t_map.get(leftChar)) {
          have--;
        }
      }
      window_start++;
    }
  }
  //! if no valid window, return empty string else return the substring
  return resLen === Number.MAX_VALUE ? "" : s.slice(res[0], res[1] + 1);
};

console.log(minWindow("ADOBECODEBANC", "ABC"));
