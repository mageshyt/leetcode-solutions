`Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []`;

const rightSideView = (root) => {
  const result = [];

  const dfs = (node, depth = 0) => {
    if (!node) return;
    if (depth >= result.length) result.push(node.val);
    dfs(node.right, depth + 1);
    dfs(node.left, depth + 1);
  };
  dfs(root);
  return result;
};
