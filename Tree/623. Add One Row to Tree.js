`Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
`;

const addOneRow = (root, val, depth) => {
  const dfs = (node, d) => {
    if (!node) return;
    if (d === depth - 1) {
      const left_node = new TreeNode(val);
      const right_node = new TreeNode(val);
      // now left node is the left child of the current node
      left_node.left = node.left;
      // now right node is the right child of the current node
      right_node.right = node.right;
      // now the left child of the current node is the left_node
      node.left = left_node;
      // now the right child of the current node is the right_node
      node.right = right_node;
    }
    dfs(node.left, d + 1); // go to the left child of the current node and increase the depth by 1
    dfs(node.right, d + 1); // go to the right child of the current node and increase the depth by 1
  };
  if (depth === 1) {
    const newRoot = new TreeNode(val);
    newRoot.left = root;
    return newRoot;
  }
  dfs(root, 1);
  return root;
};
