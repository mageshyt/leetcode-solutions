`Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].`;

const runningSum = (nums) => {
  let prefix_sum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    prefix_sum += nums[i];

    nums[i] = prefix_sum;

    
  }

  return nums;
};
console.log(runningSum([1, 2, 3, 4]));
