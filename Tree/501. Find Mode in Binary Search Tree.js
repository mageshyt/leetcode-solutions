`   Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
 `;

const findMode = (root) => {
  const map = new Map();

  const dfs = (node) => {
    if (!node) return;
    map.set(node.val, map.get(node.val) + 1 || 1);
    dfs(node.left);
    dfs(node.right);
  };
  dfs(root);

  const max = Math.max(...map.values());
  const result = [];

  for (let [key, value] of map) {
    if (value === max) result.push(key);
  }
  return result;
};
