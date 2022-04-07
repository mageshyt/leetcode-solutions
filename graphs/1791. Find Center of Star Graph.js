`here is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1`;

const findCenter = (edges) => {
  const adj_list = new Map();
  for (let [u, v] of edges) {
    if (!adj_list.has(u)) adj_list.set(u, []);
    if (!adj_list.has(v)) adj_list.set(v, []);
    adj_list.get(u).push(v);
    adj_list.get(v).push(u);
  }
  let center = 0;
  let node_len = edges.length + 1;
  for (let [u, v] of adj_list) {
    if (v.length === node_len - 1) {
      center = u;
      break;
    }
  }
  return center;
};
console.log(
  findCenter([
    [1, 2],
    [2, 3],
    [4, 2],
  ])
);
