`Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true`;

const canConstruct = (ransomNote, magazine) => {
  const hash = new Map();
  for (let i = 0; i < magazine.length; i++) {
    if (hash.has(magazine[i])) {
      hash.set(magazine[i], hash.get(magazine[i]) + 1);
    } else {
      hash.set(magazine[i], 1);
    }
  }

  for (let i = 0; i < ransomNote.length; i++) {
    if (!hash.has(ransomNote[i])) {
      return false;
    } else if (hash.get(ransomNote[i]) === 0) {
      return false;
    } else {
      hash.set(ransomNote[i], hash.get(ransomNote[i]) - 1);
    }
  }
  return true;
};
console.log(canConstruct("a", "b"));
console.log(canConstruct("aa", "ab"));
console.log(canConstruct("aa", "aab"));
