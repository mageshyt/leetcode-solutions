`Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

 

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4`;
const splitArray = (nums, m) => {
  const max = Math.max(...nums);
  const sum = nums.reduce((acc, cur) => acc + cur, 0);
  let left = max;
  let right = sum;
  let res = right;
  //! helper function
  const canSplit = (largest) => {
    let subarrays = 0;
    let currSum = 0;
    for (let num of nums) {
      currSum += num;
      if (currSum > largest) {
        currSum = num;
        subarrays++;
      }
    }
    return subarrays + 1 <= m;
  };
  while (left <= right) {
    let mid = Math.floor((right + left) / 2);
    if (canSplit(mid)) {
      res = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return res;
};
console.log(splitArray([1, 2, 3, 4, 5], 2));
