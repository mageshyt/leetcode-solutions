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

const permute = (nums: number[]): number[][] => {
  const result: number[][] = [];

  const permuteHelper = (nums: number[], path: number[]) => {
    if (nums.length === 0) {
      result.push(path);
      return;
    }

    for (let i = 0; i < nums.length; i++) {
      const newArray = [...nums];
      newArray.splice(i, 1);
      permuteHelper(newArray, [...path, nums[i]]);
    }

    return;
  };

  permuteHelper(nums, []);

  return result;
};

console.log(permute([1, 2, 3]));
