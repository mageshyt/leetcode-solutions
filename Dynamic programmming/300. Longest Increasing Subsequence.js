`Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104`;

const lengthOfLIS = (nums) => {
  const dp = new Array(nums.length).fill(1);
  for (let num = nums.length - 1; num >= 0; num--) {
    for (let next = num + 1; next < nums.length; next++) {
      if (nums[next] > nums[num]) {
        dp[num] = Math.max(dp[num], dp[next] + 1);
      }
    }
  }
  return Math.max(...dp);
};
console.log(lengthOfLIS([1, 3, 5, 4, 7]));

console.log(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]));

//! brute force

const bruteForce = (nums) => {
  let res = 1;

  for (let i = 0; i < nums.length; i++) {
    let count = 1;
    let max = nums[i];
    for (let j = i + 1; j < nums.length; j++) {
      if (max < nums[j]) {
        max = nums[j];
        count++;
      }
    }

    res = Math.max(count, res);
  }
  return res;
};

// console.log(bruteForce([1, 3, 5, 4, 7]));

// console.log(bruteForce([7, 7, 7, 7, 7, 7, 7]));
console.log(bruteForce([10, 9, 2, 5, 3, 7, 101, 18]));
