`Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
`;

const commonChars = (words) => {
  let prevMap = new Map();

  let word1 = words[0];
  for (let char of word1) {
    prevMap.set(char, prevMap.get(char) + 1 || 1);
  }
  //! start loop from second word
  for (let word of words.slice(1)) {
    const currentMap = new Map();
    for (let char of word) {
      if (prevMap.has(char)) {
        currentMap.set(char, currentMap.get(char) + 1 || 1);
        prevMap.get(char) > 1
          ? prevMap.set(char, prevMap.get(char) - 1)
          : prevMap.delete(char);
      }
    }
    prevMap = currentMap;
  }
  let result = [];
  prevMap.forEach((val, key) => {
    while (val) {
      result.push(key);
      --val;
    }
  });

  return result;
};
console.log(commonChars(["bella", "label", "roller"]));
