`Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty
word in s.

Example 1:
  Input: pattern = "abba", s = "dog cat cat dog"
  Output: true
Example 2:
  Input: pattern = "abba", s = "dog cat cat fish"
  Output: false
Example 3:
  Input: pattern = "aaaa", s = "dog cat cat dog"
  Output: false`;

const wordPattern = (pattern, str) => {
  const hash1 = {};
  const hash2 = {};
  for (let i = 0; i < pattern.length; i++) {
    const char = pattern[i];
    if (!hash1[char]) {
      hash1[char] = [i];
    } else {
      hash1[char] = hash1[char].concat(i);
    }
  }
  const words = str.split(" ");
  for (let i = 0; i < words.length; i++) {
    const word = words[i];
    if (!hash2[word]) {
      hash2[word] = [i];
    } else {
      hash2[word] = hash2[word].concat(i);
    }
  }

  if (Object.keys(hash1).length !== Object.keys(hash2).length) return false;
  const values1 = Object.values(hash1);
  const values2 = Object.values(hash2);
  console.log(values1, values2);
  // check if all values are the same in 2 object
  for (let i = 0; i < values1.length; i++) {
    if (values1[i].length !== values2[i].length) return false;
    for (let j = 0; j < values1[i].length; j++) {
      if (values1[i][j] !== values2[i][j]) return false;
    }
  }
  return true;
};
(pattern = "aaaa"), (s = "dog cat cat dog");
console.log(wordPattern(pattern, s));
