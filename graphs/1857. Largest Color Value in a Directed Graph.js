const largestPathValue = (colors, edges) => {
  const n = colors.length;

  const adj = new Map();

  for (let i = 0; i < n; i++) {
    adj.set(i, []);
  }

  for (const [u, v] of edges) {
    adj.get(u).push(v);
  }

  const color_count = new Array(n).fill(0).map(() => new Array(26).fill(0)); // [node][color] = count

  let res = 0;

  const visited = new Set();

  const path = new Set();

  const dfs = (node) => {
    if (path.has(node)) return Number.MAX_SAFE_INTEGER; // cycle detected

    if (visited.has(node)) return 0; // already visited

    visited.add(node); // mark as visited
    path.add(node); // add to path

    const color = colors.charCodeAt(node) - 97; // get color

    color_count[node][color] = 1; // fist time visiting this node

    for (const next of adj.get(node)) {
      if (dfs(next) === Number.MAX_SAFE_INTEGER) return Number.MAX_SAFE_INTEGER; // cycle detected

      for (let c = 0; c < 26; c++) {
        color_count[node][c] = Math.max(
          color_count[node][c],
          color_count[next][c] + (c == color ? 1 : 0)
        ); // update color count
      }
    }

    path.delete(node); // remove from path

    return Math.max(...color_count[node]); // return max color count
  };

  for (let node = 0; node < n; node++) {
    res = Math.max(res, dfs(node));
  }

  return res === Number.MAX_SAFE_INTEGER ? -1 : res; // if no path
};

const colors = "abaca";
const edges = [
  [0, 1],
  [0, 2],
  [2, 3],
  [3, 4],
];

console.log("👉 Output: ", largestPathValue(colors, edges));
