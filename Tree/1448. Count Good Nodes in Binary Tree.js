`Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.`;

const goodNodes = (root) => {
  const dfs = (node) => {
    if (!node) return 0;
    const node_val = node.val;
    let good = node_val >= max ? 1 : 0;
    max = Math.max(max, node_val);
    good += dfs(node.left);
    good += dfs(node.right);
  };
  return dfs(root);
};
