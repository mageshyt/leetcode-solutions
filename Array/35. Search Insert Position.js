// Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.

// Example 1:

// Input: nums = [1,3,5,6], target = 5
// Output: 2
// Example 2:

// Input: nums = [1,3,5,6], target = 2
// Output: 1
// Example 3:

// Input: nums = [1,3,5,6], target = 7
// Output: 4
// Example 4:

// Input: nums = [1,3,5,6], target = 0
// Output: 0
var searchInsert = function (nums, target) {
  let pointer = 0;
  let pointer2 = nums[nums.length - 1];
  if (nums.length === 0) {
    return 0;
  }
  while (pointer < nums.length) {
    if (target === nums[pointer]) {
      return pointer;
    } else if (target < nums[pointer]) {
      return pointer;
    } else if (target > pointer2) {
      return nums.length;
    }

    pointer++;
  }
};
nums = [1, 3, 5, 7];
console.log(searchInsert(nums, 2));
console.log(searchInsert(nums, 7));

const searchInsert2 = (nums, target) => {
  let left = 0;
  let right = nums.length - 1;
  while (left <= right) {
    const mid = Math.floor(left + (right - left) / 2);
    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return left;
};

console.log(searchInsert2(nums, 2));
console.log(searchInsert2(nums, 7));
