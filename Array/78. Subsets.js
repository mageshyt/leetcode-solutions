`Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]`;

const subsets = (nums) => {
  let tempDataStruct = [];
  const result = [];
  let idx = 0;
  const helper = (stack, index) => {
    result.push([...stack]);
    for (let i = index; i < nums.length; i++) {
      stack.push(nums[i]);
      helper(stack, i + 1);
      stack.pop();
    }
  };
  helper(tempDataStruct, idx);
  return result;
};

console.log(subsets([1, 2, 3]));
