`The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!`;

const getPermutation = (n, k) => {
  const res = [];
  const nums = [...Array(n).keys()].map((i) => i + 1);
  const backtracking = (per) => {
    if (per.length === n) {
      res.push([...per]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      const topVal = nums[i];
      const prevVal = nums[i - 1];
      if (topVal === null || topVal === prevVal) {
        continue;
      }
      nums[i] = null; //! mark as visited
      // ! push the topVal to the permutation
      per.push(topVal);
      // ! recursion
      backtracking(per);
      // ! pop the topVal from the permutation
      console.log({ before: per });
      per.pop();
      console.log({ after: per });

      // ! unmark as visited
      nums[i] = topVal;
    }
  };
  backtracking([]);
  return res[k - 1].join("");
};

console.log(getPermutation(3, 3));
