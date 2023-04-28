const numSimilarGroups = (words) => {
  const len = words.length;

  const visited = new Set();

  let groups = 0;

  for (let i = 0; i < len; i++) {
    // if i is already seen then skip
    if (!visited[i]) {
      groups += 1;

      dfs(i, visited, words);
    }
  }

  console.log("👉 visited", visited);

  return groups;
};

const dfs = (start, visited, words) => {
  // mark as visited
  visited[start] = true;

  for (let i = 0; i < words.length; i++) {
    // if i is already seen then skip
    if (visited[i]) continue;

    if (is_simiar(words[start], words[i])) {
      dfs(i, visited, words);
    }
  }
};

const is_simiar = (w1, w2) => {
  let count = 0;
  for (let i = 0; i < w1.length; i++) {
    if (count > 3) return false;

    if (w1[i] == w2[i]) {
      count += 1;
    }
  }

  return count == 0 || count == 2;
};

const strs = ["tars", "rats", "arts", "star"];

console.log(numSimilarGroups(strs));
