const findLadders = (beginWord, endWord, wordList) => {
  // to check if two words can connect
  let connected = (a, b) => {
    let c = 0;
    for (let i = 0; i < a.length && c < 2; i++) {
      if (a[i] !== b[i]) c++;
    }
    return c == 1;
  };

  let dict = new Set(wordList); // to check if a word is in the dictionary
  if (dict.has(endWord) == false) return []; // if endWord is not in the dictionary, return empty array

  dict.delete(beginWord);
  let queue = [beginWord];
  let paths = [];

  let reached = false;
  while (queue.length && !reached) {
    // update points of paths for this level
    paths.push(queue.slice());

    // access whole level
    let q_len = queue.length;
    for (let i = 0; i < q_len && !reached; i++) {
      let from = queue.shift();
      for (let to of dict) {
        if (connected(from, to) == false) continue; // if two words can't connect, skip

        if (to == endWord) {
          reached = true;
          break;
        }

        queue.push(to); // add to the queue

        // and delete "to" from dict to prevent a cycle
        dict.delete(to);
      }
    }
  }

  // scanned all but did not see endWord in paths
  if (!reached) return [];

  let ans = [[endWord]]; // initialize the answer with the endWord
  for (let level = paths.length - 1; level >= 0; level--) {
    // from the last level to the first
    let a_len = ans.length;
    for (let a = 0; a < a_len; a++) {
      let p = ans.shift();
      let last = p[0];
      for (let word of paths[level]) {
        if (!connected(last, word)) continue;
        ans.push([word, ...p]);
      }
    }
  }

  return ans;
};
