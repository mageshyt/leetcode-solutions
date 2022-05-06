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

      if (current === word) {
        temp = word;
        break;
      }
    }
    res.push(temp);
  }
  return res.join(" ");
};