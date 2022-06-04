`Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

`;

const subsetsWithDup = (nums) => {
  const result = [];
  nums.sort((a, b) => a - b);
  const backtracking = (subset, index) => {
    if (index === nums.length) {
      result.push([...subset]);
      return;
    }

    //! All subsets that include subset[index]
    subset.push(nums[index]);
    backtracking(subset, index + 1);
    //! before that we should remove the value we added in sub set
    subset.pop();
    //! all subsets that not include

    while (index + 1 < nums.length && nums[index + 1] === nums[index]) {
      //! to skip the duplicates
      index++;
    }
    backtracking(subset, index + 1);
  };
  backtracking([], 0);
  return result;
};

console.log(subsetsWithDup([1, 2, 2]));
