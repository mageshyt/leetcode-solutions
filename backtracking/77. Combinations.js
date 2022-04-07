`Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]`;

const combine = (n, k) => {
  const res = [];
  const backtracking = (per, start) => {
    if (per.length === k) {
      //   console.log(per);
      res.push([...per]);
      return;
    }
    for (let i = start; i <= n; i++) {
      per.push(i);
      //   console.log({ i, per });
      backtracking(per, i + 1);
      per.pop();
    }
  };
  backtracking([], 1);
  return res;
};
console.log(combine(20, 16));
