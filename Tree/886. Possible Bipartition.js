`We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
`;

const possibleBipartition = (n, dislikes) => {
  if (!dislikes.length) return true;

  const graph = new Map(); // create graph with n + 1 nodes

  const visited = new Array(n + 1).fill(0);
  const stack = [];

  for (const [a, b] of dislikes) {
    if (!graph.has(a)) graph.set(a, []);
    if (!graph.has(b)) graph.set(b, []);

    graph.get(a).push(b);
    graph.get(b).push(a);
  }

  visited[0] = 1;

  stack.push([dislikes[0][0], 1]); // mark first node as visited

  while (stack.length > 0) {
    const [node, mark] = stack.pop();
    console.log(node, mark);

    visited[node] = mark;

    if (!graph.has(node)) continue;

    for (const neighbor of graph.get(node)) {
      if (visited[neighbor] === mark) return false;

      if (visited[neighbor] === 0) {
        stack.push([neighbor, mark === 1 ? 2 : 1]);
      }
    }
    if (stack.length === 0 && visited.includes(0)) {
      for (let i = 1; i <= n; i++) {
        if (visited[i] === 0) {
          stack.push([i, 1]);
          break;
        }
      }
    }
  }

  return true;
  // return checkBipartition(graph, n);
};

const n = 5;

const dislikes = [
  [1, 2],
  [1, 3],
  [2, 4],
];
console.log(possibleBipartition(n, dislikes));
