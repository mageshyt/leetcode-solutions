`Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


`;

const permute = (nums) => {
  const res = [];
  //! base base
  if (nums.length === 1) {
    const cpy = [...nums];
    console.log(cpy);
    return [cpy];
  }
  //! recursion
  for (let i = 0; i < nums.length; i++) {
    const topVal = nums.shift();
    const subRes = permute(nums); // subRes is an array of arrays which is the result of permute(nums)
    for (let num of subRes) {
      num.push(topVal);
    }
    console.log({ subRes });
    res.push(...subRes);
    nums.push(topVal);
  }
  return res;
};

console.log(permute([1, 2, 3]));
