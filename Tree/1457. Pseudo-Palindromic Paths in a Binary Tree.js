`Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).`;

const pseudoPalindromicPaths = (root) => {
  const dfs = (node, path) => {
    if (!root) return 0;

    //! 1. add current val node to path if it was not there
    //  2. if it was there, remove it
    const val = node.val;
    if (path.has(val)) {
      path.delete(val);
    } else {
      path.add(val);
    }

    //! 3. if it is a leaf node, check if path is a palindrome
    if (!node.left && !node.right) {
      return path.size <= 1 ? 1 : 0;
    }

    const left = dfs(node.left, new Set(path));
    const right = dfs(node.right, new Set(path));
    
    return left + right;
  };
  return dfs(root, new Set());
};
