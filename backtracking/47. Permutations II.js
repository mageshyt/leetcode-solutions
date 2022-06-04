`Given a collection of numbers, nums,
 that might contain duplicates,
  return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`;
//! solution 1
const permuteUnique = (nums) => {
  const res = [];
  nums.sort((a, b) => a - b);
  const backtracking = (per) => {
    if (per.length === nums.length) {
      res.push([...per]);
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
      per.pop();
      // ! unmark as visited
      nums[i] = topVal;
    }
    //! base base
  };
  backtracking([]);
  return res;
};

//! solution 2
const permuteUnique2 = (nums) => {
  const result = [];
  const perm = []; //! our permutation
  const map = new Map();
  //! lets hash our nums
  for (let num of nums) {
    map.set(num, map.get(num) + 1 || 1);
  }
  const backtrackingDFS = () => {
    if (nums.length === perm.length) {
      const cp = [...perm];
      result.push(cp);
      return;
    }
    for (let [num, count] of map) {
      if (map.get(num) > 0) {
        perm.push(num);
        //! decrement the count
        map.set(num, map.get(num) - 1);
        backtrackingDFS();
        //! increment the count
        map.set(num, map.get(num) + 1);
        perm.pop();
      }
    }
  };
  backtrackingDFS();
  return result;
};
console.log(permuteUnique2([2, 2, 1, 1]));
