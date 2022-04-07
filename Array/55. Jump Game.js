`You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.`;

const canJump = (nums) => {
  let goalPost = nums.length - 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    console.log({ i, goalPost, num: i + nums[i] });
    if (i + nums[i] >= goalPost) {
      // ! if our current index + the current jump length is greater than the goal post, we can jump to the goal post
      goalPost = i;
    }
  }
  return goalPost === 0;
};
console.log(canJump([2, 3, 1, 1, 4]));
