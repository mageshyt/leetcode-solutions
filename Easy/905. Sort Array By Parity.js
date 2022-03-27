`Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.`;
const sortArrayByParity = (nums) => {
  let p = 0;
  let len = nums.length;
  for (let i = 0; i < len; i++) {
    if (nums[i] % 2 === 0) {
      [nums[i], nums[p]] = [nums[p], nums[i]];
      p++;
    }
  }
  return nums;
};

console.log(sortArrayByParity([3, 1, 2, 4]));
