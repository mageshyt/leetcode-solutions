`Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.`;

const rangeSumBST = (root, low, high) => {
  let ans = 0;
  const helper = (node) => {
    const stack = [node];
    while (stack.length > 0) {
      const curr = stack.pop();
      if (curr.val >= low && curr.val <= high) {
        ans += curr.val;
      }
      if (curr.left) {
        stack.push(curr.left);
      }
      if (curr.right) {
        stack.push(curr.right);
      }
    }
  };
  helper(root);
  return ans;
};
