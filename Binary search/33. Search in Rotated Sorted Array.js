`here is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1`;

const search = (nums, target) => {
  
  let left=0;
  let right=nums.length-1;

  while(left<=right){
    const mid=Math.floor((left+right)/2);
    // ! if mid is target then return mid
    if(nums[mid]===target) return mid;

    // ! if left is sorted
    if(nums[left]<=nums[mid]){
      // if target is greater than mid 
      if (target > nums[mid] || target < nums[left]){
        left=mid+1;
      }
      else{
        right=mid-1;
      }

    }
    // ! if right is sorted
    else{
      if(target < nums[mid] || target > nums[right]){
        right=mid-1;
      }
      else{
        left=mid+1;
      }
    }
  }
  return -1;
};

console.log(search([4, 5, 6, 7, 0, 1, 2], 0));

//! binary search

const search2 = (nums, target) => {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) return mid;
    // ! left sorted nums
    if (nums[left] <= nums[mid]) {
      if (target > nums[mid] || target < nums[left]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    //! right sorted nums
    else {
      if (target < nums[mid] || target > nums[right]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
  }
  return -1;
};

console.log(search2([4, 5, 6, 7, 0, 1, 2], 0));
