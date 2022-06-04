`Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

 

Example 1:


Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
Example 2:


Input: tree = [7], target =  7
Output: 7`;

const isSameTree = (original, cloned) => {
  const q1 = [original];
  const q2 = [cloned];
  while (q1.length > 0 && q2.length > 0) {
    const o = q1.shift(); // original
    const c = q2.shift(); // cloned
    if (o === null && c === null) continue;
    if (o.val !== c.val) return false;
    if (o.left !== null) {
      q1.push(o.left);
      q2.push(c.left);
    }
    if (o.right !== null) {
      q1.push(o.right);
      q2.push(c.right);
    }
  }
  return true;
};

const getTargetCopy = (original, cloned, target) => {
  const o = [original]; // original
  const c = [cloned]; // cloned
  while (o.length > 0 && c.length > 0) {
    const o1 = o.shift(); // original
    const c1 = c.shift(); // cloned
    if (o1 === null && c1 === null) continue;
    if (o1.val === target.val) return c1;
    if (o1.left !== null) {
      o.push(o1.left);
      c.push(c1.left);
    }
  }
    return null;
};
