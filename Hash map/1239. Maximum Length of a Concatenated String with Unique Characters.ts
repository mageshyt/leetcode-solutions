`You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.`;

const maxLength = (arr: string[]): number => {
  //! base case
  if (arr.length === 0) return 0;
  if (arr.length === 1) return isUnique(arr[0]) ? arr[0].length : 0;
  let maxLen = Number.NEGATIVE_INFINITY;


  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      const str = arr[i] + arr[j];
      if (isUnique(str)) maxLen = Math.max(maxLen, str.length);
    }
  }
  return maxLen;
};

const isUnique = (str: string): boolean => {
  const set = new Set();
  for (let i = 0; i < str.length; i++) {
    if (set.has(str[i])) return false;
    set.add(str[i]);
  }
  return true;
};

console.log(maxLength(["un", "iq", "ue"]));
console.log(maxLength(["cha", "r", "act", "ers"]));
console.log(maxLength(["abcdefghijklmnopqrstuvwxyz"]));
