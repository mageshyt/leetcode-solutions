`You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
`;

const getMax = (map) => Math.max(...Array.from(map.values()));

const characterReplacement = (s, k) => {
  const map = new Map();
  let max_len = 0;

  let windowStart = 0;

  for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
    const char = s[windowEnd];
    map.set(char, map.get(char) + 1 || 1);
    const windowSize = windowEnd - windowStart + 1;
    console.log("max_len", getMax(map), map, windowSize);
    if (windowSize - getMax(map) <= k) {
      max_len = Math.max(max_len, windowSize);
    }

    if (windowSize - getMax(map) > k) {
      //! delete the leftmost character
      map.set(s[windowStart], map.get(s[windowStart]) - 1);
      windowStart++;
    }
  }
  return max_len;
};

console.log(characterReplacement("ABAB", 2));
console.log(characterReplacement("AABABBA", 1));
