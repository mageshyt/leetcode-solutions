`Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]`;

const binaryTreePaths = (root) => {
  const result = [];
  const path = [];
  const dfs = (node, path) => {
    if (!node) return;
    path.push(node.val);
    if (!node.left && !node.right) {
      result.push(path.join("->"));
    } else {
      dfs(node.left, path);
      dfs(node.right, path);
    }
    path.pop();
  };
  dfs(root, path);
  return result;
};
