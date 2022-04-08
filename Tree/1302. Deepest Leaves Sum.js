`Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 `;

const MaxDepth = (root) => {
  let depth = 0;

  const stack = [root];
  while (stack.length > 0) {
    const node = stack.pop();
    if (node.left) {
      stack.push(node.left);
    }
    if (node.right) {
      stack.push(node.right);
    }

    depth++;
  }
  return Math.floor(depth / 2);
};
const deepestLeavesSum = (root) => {
  let sum = 0;
  let max_dep = 0;
  const bfs = (head, depth) => {
    if (depth > max_dep) {
      max_dep = depth;
      sum = 0;
    }
    if (depth === max_dep) {
      sum += head.val;
    }
    if (head.left !== null) bfs(head.left, depth + 1);
    if (head.right !== null) bfs(head.right, depth + 1);
  };
  bfs(root, 1);
  return sum;
};
