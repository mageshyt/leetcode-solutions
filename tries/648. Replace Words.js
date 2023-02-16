`n English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"`;

const replaceWords = (dictionary, sentence) => {
  const map = new Map();
  for (let word of dictionary) {
    map.set(word, word.length);
  }

  const res = [];

  for (let word of sentence.split(" ")) {
    let temp = word;
    for (let [word, length] of map) {
      const current = temp.slice(0, length);
      let len = current.length;
      if (current === word) {
        //! make temp as short len word
        if (temp.length > len) {
          temp = word;
        }
      }
    }
    res.push(temp);
  }
  return res.join(" ");
};

console.log(
  replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
);

const dic = ["catt", "cat", "bat", "rat"];
const sen = "the cattle was rattled by the battery";
console.log(replaceWords(dic, sen));
