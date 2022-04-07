// Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

// If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

// The replacement must be in place and use only constant extra memory.

// Example 1:

// Input: nums = [1,2,3]
// Output: [1,3,2]
// Example 2:

// Input: nums = [3,2,1]
// Output: [1,2,3]
// Example 3:

// Input: nums = [1,1,5]
// Output: [1,5,1]
// Example 4:

// Input: nums = [1]
// Output: [1]

var nextPermutation = function (nums) {
  let right = nums.length - 1;
  let pointer = right - 1;
  while (pointer >= 0 && nums[pointer] >= nums[pointer + 1]) {
    pointer--;
    // return pointer;
  }
  if (pointer >= 0) {
    while (right >= 0 && nums[right] <= nums[pointer]) right--;
    swap(nums, right, pointer);
  }
  reverse(nums, pointer + 1);
  function swap(nums, pointer, right) {
    let temp = nums[pointer];
    nums[pointer] = nums[right];
    nums[right] = temp;
  }
  function reverse(nums, start) {
    let end = nums.length - 1;
    while (start < end) {
      swap(nums, start, end);
      start++;
      end--;
    }
  }
  return nums;
};

console.log(nextPermutation([1, 2, 3]));
