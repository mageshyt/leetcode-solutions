`A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.`;

const maxPathSum = (root) => {
  const ans = [root.val]; // root.val is the max path sum of the root
  const dfs = (node) => {
    if (!node) return 0;

    // we are going to find max sun of left and right child
    const leftMax = dfs(node.left); // to avoid negative number we are using Math.max
    const rightMax = Math.max(dfs(node.right), 0); //! to avoid negative number we are using Math.max

    // to compute the max sum we need to spit the max sum of left and right child
    ans[0] = Math.max(ans[0], leftMax + rightMax + node.val);
    return Math.max(leftMax, rightMax) + node.val;
  };
  dfs(root);
};
