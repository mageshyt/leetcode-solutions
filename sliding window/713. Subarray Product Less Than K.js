`Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0`;

const numSubarrayProductLessThanK = (nums, k) => {
  if (k === 0) return 0;
  let count = 0;
  let i = 0;
  while (i < nums.length) {
    let curr_prod = 1;
    for (let j = i; j < nums.length; j++) {
      curr_prod *= nums[j];
      if (curr_prod < k) count++;
      else break;
    }
    i++;
  }

  return count;
};
console.log(numSubarrayProductLessThanK([10, 5, 2, 6], 100));
console.log(numSubarrayProductLessThanK([1, 2, 3], 0));
console.log(numSubarrayProductLessThanK([1, 1, 1], 1));
