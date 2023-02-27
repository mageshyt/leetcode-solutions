`Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

 

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].`;

const leftRigthDifference = (nums) => {
  let left_sum = nums.reduce((a, b) => a + b, 0);
  let right_sum = nums.reduce((a, b) => a + b, 0);

  const leftsum_array = new Array(nums.length).fill(0);
  const rightsum_array = new Array(nums.length).fill(0);

  const ans = new Array(nums.length).fill(0);
  for (let i = 0; i < nums.length; i++) {
    left_sum -= nums[i];
    right_sum -= nums[nums.length - 1 - i];

    leftsum_array[i] = left_sum;
    rightsum_array[nums.length - 1 - i] = right_sum;
  }

  for (let i = 0; i < nums.length; i++) {
    ans[i] = Math.abs(leftsum_array[i] - rightsum_array[i]);
  }

  return ans;
};

console.log(leftRigthDifference([10, 4, 8, 3]));

const generateRandomNumber = () => {
  if (gameStart) {
    setTimeout(() => {
      setRandomNumber(random);
    }, 2000);
  }
};
