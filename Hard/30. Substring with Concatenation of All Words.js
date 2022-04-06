`You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]`;

const findSubstring = (s, words) => {
  const map = new Map();
  const len = words.length;
  const wordLen = words[0].length;
  const totalLen = len * wordLen; //! all of the word going to have same length
  const res = [];
  for (const word of words) {
    map.set(word, map.get(word) + 1 || 1);
  }
  // ! Lets declare leftIdx and right Idx

  let leftIdx = 0; //! string
  let rightIdx = totalLen - 1; //! total length of needed string -1
  //! helper function
  const helper = (tempStr) => {
    const visited = new Map();
    const len = tempStr.length; //! substring length
    for (let i = 0; i < len; i += wordLen) {
      const word = tempStr.substr(i, wordLen);
      if (!map.has(word)) return false;
      visited.set(word, (visited.get(word) || 0) + 1);
    }
    for (let [word, idx] of visited) {
      if (map.get(word) !== idx) {
        return false;
      }
    }
    return true;
  };

  while (rightIdx < s.length) {
    if (rightIdx - leftIdx + 1 === totalLen) {
      let temp = s.substring(leftIdx, rightIdx + 1); // get the substring from left to right idx +1

      console.log({ temp, leftIdx, rightIdx });
      if (helper(temp)) res.push(leftIdx);
      leftIdx++;
    }
    rightIdx++;
  }
  return res;
};
console.log(findSubstring("barfoothefoobarman", ["foo", "bar"]));
