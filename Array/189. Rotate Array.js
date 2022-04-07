`Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]`;
const reverse_Helper = (nums, start, end) => {
  while (start < end) {
    [nums[start], nums[end]] = [nums[end], nums[start]];
    `
    Here we are swapping the first elements of the array with the last elements of the array.
    `;
    start++;
    end--;
  }
  //   console.log("nums 👉", nums);
  return nums;
};
const rotate = (nums, k) => {
  k = k % nums.length;
  console.log("k 👉", k);
  reverse_Helper(nums, 0, nums.length - 1);

  reverse_Helper(nums, 0, k - 1);

  reverse_Helper(nums, k, nums.length - 1);

  return nums;
};
(nums = [-1, -100, 3, 99]), (k = 2);
console.log(rotate(nums, k));
