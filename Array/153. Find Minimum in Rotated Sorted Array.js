`Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. `;

const findMin = (nums) => {
  let left = 0;
  let right = nums.length - 1;

  if (nums[left] < nums[right]) {
    //! it mean our array is sorted
    return leftVal;
  }
  while (left < right) {
    const mid = Math.floor((left + right) / 2); //we will get mid value
    if (nums[mid] > nums[mid + 1]) {
      //! we will check if middle is greater than next value
      // ! if it is we will return next value and it should be smallest
      return nums[mid + 1];
    }
    if (nums[mid] < nums[mid - 1]) {
      //! we will check if middle is less than previous value
      // ! if it is we will return previous value and it should be smallest
      return nums[mid];
    }
    if (nums[mid] > 0) {
      //! if middle is greater than 0

      left = mid + 1;
    } else {
      right = mid - 1;
      //! if middle is less than 0 then small value will be somewhere in left side
    }
  }
  return -1;
};

console.log(findMin([3, 4, 5, 1, 2]));
