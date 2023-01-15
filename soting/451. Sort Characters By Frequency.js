`Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.`;

const frequencySort = (s) => {
  const map = new Map();
  for (let i = 0; i < s.length; i++) {
    const current = s[i];
    // get ASCII value
    const ascii = current.charCodeAt(0);

    // if not in map
    if (!map.has(current)) {
      map.set(current, [1, ascii]);
    } else {
      map.set(current, [map.get(current)[0] + 1, ascii]);
    }
  }
  // sort by frequency
  const sorted = [...map.entries()].sort((a, b) => b[1][0] - a[1][0]);
  let result = "";
  for (let i = 0; i < sorted.length; i++) {
    let [char, [freq, ascii]] = sorted[i];
    result += char.repeat(freq);
  }
  return result;
};

console.log(frequencySort("tree"));
